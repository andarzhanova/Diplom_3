import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Нажимаем кнопку «Восстановить пароль»')
    def click_restore_password_button(self):
        self.wait_for_element_to_be_clickable(LoginPageLocators.RESTORE_PASSWORD_LINK)
        self.click_on_element(LoginPageLocators.RESTORE_PASSWORD_LINK)

    @allure.step('Нажимаем на поле "email"')
    def click_email_field(self):
        self.wait_for_element_to_be_clickable(LoginPageLocators.EMAIL)
        self.click_on_element(LoginPageLocators.EMAIL)

    @allure.step('Заполняем поле "email"')
    def set_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL, email)

    @allure.step('Нажимаем на поле "Пароль"')
    def click_pass_field(self):
        self.click_on_element(LoginPageLocators.PASSWORD)

    @allure.step('Заполняем поле "Пароль"')
    def set_pass(self, password):
        self.send_keys(LoginPageLocators.PASSWORD, password)

    @allure.step('Нажимаем кнопку «Войти»')
    def click_login_button(self):
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Авторизуемся')
    def login(self, email, password):
        self.click_email_field()
        self.set_email(email)
        self.click_pass_field()
        self.set_pass(password)
        self.click_login_button()

    @allure.step('Проверяем переход на страницу Вход')
    def check_switch_on_login_page(self):
        self.wait_for_visibility_of_element(LoginPageLocators.LOGIN_HEADER)
        return self.get_current_url()
