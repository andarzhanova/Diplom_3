import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.ingredient_details_pages import IngredientDetailsPage
from data.urls_constants import UrlsConstants
from data.main_page_constants import MainPageConstants
from data.ingredient_details_constants import IngredientDetailsConstants



@allure.feature('Основной функционал')
class TestBasicFunctionality:
    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description(
        'Нажимаем на кнопку «Лента Заказов» и проверяем, '
        'что произошёл переход на страницу Ленты заказов'
    )
    def test_switch_on_order_feed_click_order_feed_button_order_feed_url(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        current_url = order_feed_page.check_switch_on_order_feed()
        assert current_url == UrlsConstants.ORDER_FEED_URL

    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description(
        'Нажимаем кнопку «Конструктор» и проверяем, '
        'что произошёл переход на главную страницу'
    )
    def test_switch_on_main_page_click_constructor_button_main_page_url(self, driver):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_constructor_button()
        main_page = MainPage(driver)
        current_url = main_page.check_switch_on_main_page()
        assert current_url == MainPageConstants.MAIN_PAGE_URL

    @allure.title('Проверка появления всплывающего окна с деталями')
    @allure.description('Кликаем на ингредиент и проверяем, что появилось всплывающее окно с деталями')
    def test_window_with_details_click_on_ingredient_show_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        ingredient_details_pages = IngredientDetailsPage(driver)
        actually_text = ingredient_details_pages.check_show_window_with_details()
        assert actually_text == IngredientDetailsConstants.WINDOW_HEADER

    @allure.title('Проверка закрывания окна кликом по крестику')
    @allure.description('Кликаем по крестику и проверяем, что всплывающее окно закрылось')
    def test_window_closed_click_close_button_header_not_displayed(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        ingredient_details_pages = IngredientDetailsPage(driver)
        ingredient_details_pages.click_close_button()
        displayed = ingredient_details_pages.check_window_closed()
        assert not displayed

    @allure.title('Проверка увеличения счётчика ингридиента при добавлении в заказ')
    @allure.description(
        'Получаем значение счетчика ингредиента до и после добавления в заказ, '
        'и проверяем, что значение счетчика увеличилось'
    )
    def test_increasing_counter_add_ingredient_increasing_value(self, driver):
        main_page = MainPage(driver)
        prev_counter_value = main_page.get_count_value()
        main_page.add_ingredient()
        current_counter_value = main_page.get_count_value()
        assert current_counter_value > prev_counter_value

    @allure.title('Проверка возможности оформления заказ залогиненным пользователем')
    @allure.description(
        'Нажимаем кнопку «Оформить заказ» и проверяем, '
        ' что заказ оформлен и появился идентификатор заказа'
    )
    def test_making_an_order_click_checkout_button_show_window_with_order_id(self, authorization):
        driver = authorization
        main_page = MainPage(driver)
        main_page.add_ingredient()
        main_page.click_checkout_button()
        actually_text = main_page.check_show_window_with_order_id()
        assert actually_text == MainPageConstants.ORDER_ID
