from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, 'Личный Кабинет')  # Кнопка "Личный кабинет"
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')  # Кнопка "Лента Заказов"
    BURGER_HEADER = (By.XPATH, '//h1[text()="Соберите бургер"]')  # Заголовок "Соберите бургер"
    BUN_INGREDIENT = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]')  # Ингредиент "Флюоресцентная булка R2-D3"
    COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]')  # Счетчик
    CONSTRUCTOR_BASKET = (By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_')  # Корзина для конструктора
    CHECKOUT_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')  # Кнопка "Оформить заказ"
    ORDER_ID = (By.XPATH, '//p[text()="идентификатор заказа"]')  # Идентификатор заказа
