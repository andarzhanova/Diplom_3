import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import helpers
from data.api_constants import ApiConstants
from data.urls_constants import UrlsConstants
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.fixture(scope='class', params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        service = GeckoDriverManager().install()
        browser = webdriver.Firefox(service=Service(service))
        browser.get(UrlsConstants.STELLAR_BURGERS)
    if request.param == 'chrome':
        service = ChromeDriverManager().install()
        browser = webdriver.Chrome(service=Service(service))
        browser.get(UrlsConstants.STELLAR_BURGERS)

    yield browser
    browser.quit()


@pytest.fixture(scope='class')
def authorized_user(driver):
    payload = helpers.payload
    response = requests.post(ApiConstants.CREATE_USER, data=payload)
    main_page = MainPage(driver)
    main_page.click_personal_account_button()
    login_page = LoginPage(driver)
    login_page.login(payload["email"], payload["password"])

    yield driver
    token = response.json()['accessToken']
    requests.delete(ApiConstants.DELETE_USER, headers={'Authorization': token})


@pytest.fixture(params=['firefox', 'chrome'])
def browser(request):
    if request.param == 'firefox':
        service = GeckoDriverManager().install()
        browser = webdriver.Firefox(service=Service(service))
        browser.get(UrlsConstants.STELLAR_BURGERS)
    if request.param == 'chrome':
        service = ChromeDriverManager().install()
        browser = webdriver.Chrome(service=Service(service))
        browser.get(UrlsConstants.STELLAR_BURGERS)

    yield browser
    browser.quit()


@pytest.fixture
def user_data():
    data = []
    payload = helpers.payload
    token = requests.post(ApiConstants.CREATE_USER, data=payload).json()['accessToken']
    data.append(payload)
    data.append(token)

    yield data
    requests.delete(ApiConstants.DELETE_USER, headers={'Authorization': token})


@pytest.fixture
def authorization(browser, user_data):
    driver = browser
    payload, token = user_data
    main_page = MainPage(driver)
    main_page.click_personal_account_button()
    login_page = LoginPage(driver)
    login_page.login(payload["email"], payload["password"])
    return driver


@pytest.fixture
def orders_numbers(user_data):
    payload, token = user_data
    requests.post(ApiConstants.ORDER, headers={'Authorization': token}, data=ApiConstants.INGREDIENTS)
    requests.post(ApiConstants.ORDER, headers={'Authorization': token}, data=ApiConstants.INGREDIENTS)
    user_orders = requests.get(ApiConstants.ORDER, headers={'Authorization': token}).json()["orders"]
    orders_numbers = []
    for order in user_orders:
        orders_numbers.append(order["number"])
    return orders_numbers
