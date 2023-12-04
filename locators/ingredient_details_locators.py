from selenium.webdriver.common.by import By


class IngredientDetailsLocators:
    DETAILS_HEADER = (By.XPATH, '//h2[text()="Детали ингредиента"]')  # Заголовок "Детали ингредиента"
    CLOSE_BUTTON = (By.XPATH, '//section[contains(@class,"opened")]//button')  # Кнопка крестик
