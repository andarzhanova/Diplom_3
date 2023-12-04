from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_BUTTON = (By.LINK_TEXT, 'Профиль')  # Кнопка "Профиль"
    ORDER_HISTORY_BUTTON = (By.LINK_TEXT, 'История заказов')  # Кнопка "История заказов"
