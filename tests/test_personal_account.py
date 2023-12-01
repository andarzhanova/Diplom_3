import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_history_page import OrderHistoryPage
from pages.login_page import LoginPage


@allure.feature('Личный кабинет')
class TestPersonalAccount:
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    @allure.description(
        'Нажимаем на кнопку «Личный кабинет» и проверяем, '
        'что произошёл переход на страницу профиля'
    )
    def test_switch_on_profile_click_personal_account_button_profile_url(self, authorization):
        driver = authorization
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver)
        profile_page.check_switch_on_profile()

    @allure.title('Проверка перехода в раздел «История заказов»')
    @allure.description(
        'Нажимаем на кнопку «История заказов» и проверяем, '
        'что произошёл переход в раздел истории заказов'
    )
    def test_switch_on_order_history_click_order_history_button_order_history_url(self, authorization):
        driver = authorization
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        profile_page = ProfilePage(driver)
        profile_page.click_order_history_button()
        order_history_page = OrderHistoryPage(driver)
        order_history_page.check_switch_on_order_history()

    @allure.title('Проверка выхода из аккаунта')
    @allure.description(
        'Нажимаем на кнопку «Выход» и проверяем, '
        'что произошёл выхода из аккаунта и переход на страницу входа'
    )
    def test_log_out_click_log_out_button_order_login_url(self, authorization):
        driver = authorization
        main_page = MainPage(driver)
        main_page.click_personal_account_button()
        order_history_page = OrderHistoryPage(driver)
        order_history_page.click_log_out_button()
        login_page = LoginPage(driver)
        login_page.check_switch_on_login_page()
