import pytest
from selenium import webdriver
import helpers
from data.urls_constants import UrlsConstants
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_pass_page import ForgotPasswordPage
from data.forgot_password_constants import ForgotPasswordConstants
from data.api_requests import Requests


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.get(UrlsConstants.STELLAR_BURGERS)
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.get(UrlsConstants.STELLAR_BURGERS)

    yield browser
    browser.quit()


@pytest.fixture
def password_recovery(driver):
    main_page = MainPage(driver)
    main_page.click_personal_account_button()
    login_page = LoginPage(driver)
    login_page.click_restore_password_button()
    return driver


@pytest.fixture
def forgot_pass_page(password_recovery):
    driver = password_recovery
    forgot_pass_page = ForgotPasswordPage(driver)
    forgot_pass_page.click_email_field()
    forgot_pass_page.set_email(ForgotPasswordConstants.EMAIL)
    forgot_pass_page.click_recover_button()
    return driver


@pytest.fixture
def user_data():
    data = []
    payload = helpers.payload
    token = Requests.get_token(payload)
    data.append(payload)
    data.append(token)

    yield data
    Requests.delete_user(token)


@pytest.fixture
def authorization(driver, user_data):
    payload, token = user_data
    main_page = MainPage(driver)
    main_page.click_personal_account_button()
    login_page = LoginPage(driver)
    login_page.login(payload["email"], payload["password"])
    return driver


@pytest.fixture
def orders_numbers(user_data):
    payload, token = user_data
    Requests.create_order(token)
    Requests.create_order(token)
    user_orders = Requests.get_user_orders(token)
    orders_numbers = []
    for order in user_orders:
        orders_numbers.append(order["number"])
    return orders_numbers
