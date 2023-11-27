import allure
from locators.reset_password_locators import ResetPasswordLocators
from pages.base_page import BaselPage


class ResetPasswordPage(BaselPage):
    RESET_PASS_URL = "https://stellarburgers.nomoreparties.site/reset-password"  # URL страницы сброса пароля

    @allure.step('Проверяем переход на страницу сброса пароля')
    def check_switch_on_reset_pass(self):
        self.wait_for_element_to_be_clickable(ResetPasswordLocators.SHOW_BUTTON)
        current_url = self.get_current_url()
        assert current_url == self.RESET_PASS_URL

    @allure.step('Нажимаем кнопку «Показать пароль»')
    def click_show_button(self):
        self.click_on_element(ResetPasswordLocators.SHOW_BUTTON)

    @allure.step('Проверяем, что поле «пароль» стало активным')
    def check_pass_field_active(self):
        assert 'status_active' in self.get_attribute_value(ResetPasswordLocators.PASSWORD_FIELD, 'class')
