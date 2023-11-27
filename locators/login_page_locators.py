from selenium.webdriver.common.by import By


class LoginPageLocators:
    RESTORE_PASSWORD_LINK = (By.LINK_TEXT, 'Восстановить пароль')  # Ссылка "Восстановить пароль"
    EMAIL = (By.NAME, 'name')  # Поле для email
    PASSWORD = (By.NAME, 'Пароль')  # Поле для пароля
    LOGIN_BUTTON = (By.XPATH, '//button[(text()="Войти")]')  # Кнопка "Войти"
    LOGIN_HEADER = (By.XPATH, '.// h2[text() = "Вход"]')  # Заголовок "Вход"
