from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    PASSWORD_RECOVERY_HEADER = (By.XPATH,
                                './/h2[text() = "Восстановление пароля"]')  # Заголовок "Восстановление пароля"
    EMAIL_FIELD = (By.TAG_NAME, 'input')  # Поле "email"
    RECOVER_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')  # Кнопка "Восстановить"
