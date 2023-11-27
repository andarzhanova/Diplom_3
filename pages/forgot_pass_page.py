import allure
from locators.forgot_password_locators import ForgotPasswordLocators
from pages.base_page import BaselPage
from data.forgot_password_constants import ForgotPasswordConstants


class ForgotPasswordPage(BaselPage):
    @allure.step('Проверяем переход на страницу восстановления пароля')
    def check_switch_on_forgot_pass(self):
        self.wait_for_visibility_of_element(ForgotPasswordLocators.PASSWORD_RECOVERY_HEADER)
        current_url = self.get_current_url()
        assert current_url == ForgotPasswordConstants.FORGOT_PASS_URL

    @allure.step('Нажимаем на поле "email"')
    def click_email_field(self):
        self.wait_for_element_to_be_clickable(ForgotPasswordLocators.EMAIL_FIELD)
        self.click_on_element(ForgotPasswordLocators.EMAIL_FIELD)

    @allure.step('Заполняем поле "email"')
    def set_email(self, email):
        self.send_keys(ForgotPasswordLocators.EMAIL_FIELD, email)

    @allure.step('Нажимаем кнопку «Восстановить»')
    def click_recover_button(self):
        self.click_on_element(ForgotPasswordLocators.RECOVER_BUTTON)
