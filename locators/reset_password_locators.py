from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    SHOW_BUTTON = (By.XPATH, '//div[contains(@class,"input__icon")]/*')  # Кнопка "Показать пароль"
    PASSWORD_FIELD = (By.XPATH, '//form/fieldset[1]//div[contains(@class,"input_size_default")]')  # Поле пароль
