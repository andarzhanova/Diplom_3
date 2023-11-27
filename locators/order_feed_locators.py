from selenium.webdriver.common.by import By


class OrderFeedLocators:
    ORDER_FEED_HEADER = (By.XPATH, '//h1[text()="Лента заказов"]')  # Заголовок "Лента заказов"
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')  # Кнопка "Конструктор"
    ORDER = (By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]/li[1]')  # Заказ
    POP_UP_WINDOW = (By.XPATH, '//div[contains(@class, "Modal_order")]')  # Всплывающее окно с деталями
    ORDER_NUMBERS = (By.XPATH, '//ul//p[@class="text text_type_digits-default"]')  # Номера всех заказов в ленте
    LAST_ORDER = (By.XPATH, '//ul/li[1]//p[@class="text text_type_digits-default"]')  # Номер последнего заказа в ленте
    ALL_TIME_COUNTER = (By.CSS_SELECTOR, 'div.undefined p.OrderFeed_number__2MbrQ')  # Счётчик "Выполнено за всё время"
    TODAY_COUNTER = (By.XPATH, '//div[3]/p[contains(@class, "digits")]')  # Счётчик "Выполнено за сегодня"
    NUMBER_IN_PROGRESS = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')  # Номер в разделе "В работе"
