import allure
from pages.forgot_pass_page import ForgotPasswordPage
from pages.reset_pass_page import ResetPasswordPage
from data.forgot_password_constants import ForgotPasswordConstants
from data.urls_constants import UrlsConstants


@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description(
        'Нажимаем на кнопку «Восстановить пароль» и проверяем, '
        'что произошёл переход на страницу восстановления пароля'
    )
    def test_switch_on_forgot_pass_click_restore_pass_button_forgot_pass_url(self, password_recovery):
        driver = password_recovery
        forgot_pass_page = ForgotPasswordPage(driver)
        current_url = forgot_pass_page.check_switch_on_forgot_pass()
        assert current_url == ForgotPasswordConstants.FORGOT_PASS_URL

    @allure.title('Проверка клика по кнопке «Восстановить»')
    @allure.description(
        'Проверяем, что в результате ввода почты и нажатия на кнопку «Восстановить», '
        'произошёл переход на страницу сбрса пароля'
    )
    def test_switch_on_reset_pass_click_recover_button_reset_pass_url(self, forgot_pass_page):
        driver = forgot_pass_page
        reset_pass_page = ResetPasswordPage(driver)
        current_url = reset_pass_page.check_switch_on_reset_pass()
        assert current_url == UrlsConstants.RESET_PASS_URL

    @allure.title('Проверка клика по кнопке показать/скрыть пароль')
    @allure.description('Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_click_show_button_pass_field_active(self, forgot_pass_page):
        driver = forgot_pass_page
        reset_pass_page = ResetPasswordPage(driver)
        reset_pass_page.click_show_button()
        class_value = reset_pass_page.check_pass_field_active()
        assert 'status_active' in class_value
