from selenium.webdriver.common.by import By


class OrderHistoryLocators:
    EXIT_BUTTON = (By.XPATH, '//button[(text()="Выход")]')  # Кнопка "Выход"
    ENABLED_ORDER_HISTORY_BUTTON = (
        By.XPATH, '//ul/li[2]/a[contains(@class, "Account_link_active")]'
    )  # Включенная кнопка "История заказов"
