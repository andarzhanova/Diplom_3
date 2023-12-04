import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_locators import OrderFeedLocators


@allure.feature('Лента заказов')
class TestOrderFeed:
    @allure.title('Проверка появления всплывающего окна с деталями')
    @allure.description('Кликаем на заказ и проверяем, что появилось всплывающее окно с деталями')
    def test_window_with_details_click_on_order_show_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_on_order()
        displayed = order_feed_page.check_show_window_with_details()
        assert displayed

    @allure.title('Проверка отображения заказов пользователя в Ленте заказов')
    @allure.description(
        'Получаем номера всех заказов в Ленте, и проверяем, '
        'что номера заказов пользователя отображаются в Ленте заказов'
    )
    def test_feed_orders_user_orders_numbers_in_feed(self, authorization, orders_numbers):
        driver = authorization
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        feed_orders = order_feed_page.get_orders_numbers(orders_numbers)
        for order_number in orders_numbers:
            assert str(order_number) in feed_orders, 'Заказы пользователя не отображаются в Ленте заказов'

    @allure.title('Проверка увеличения значения счетчика заказов после создания нового заказа')
    @allure.description(
        'Получаем значение счетчика заказов до и после создания нового заказа, '
        'и проверяем, что значение счетчика увеличилось'
    )
    @pytest.mark.parametrize('counter', [OrderFeedLocators.ALL_TIME_COUNTER, OrderFeedLocators.TODAY_COUNTER])
    def test_increasing_counter_create_order_increasing_value(self, user_data, authorization, counter):
        driver = authorization
        payload, token = user_data
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        prev_counter_value = order_feed_page.get_counter_value(counter)
        order_feed_page.create_order(token)
        current_counter_value = order_feed_page.get_counter_value(counter)
        assert current_counter_value > prev_counter_value

    @allure.title('Проверка отображения номера заказа в разделе "В работе')
    @allure.description('Получаем номер нового заказа, и проверяем, что номер заказа появился в разделе "В работе"')
    def test_order_in_progress_user_order_in_progress(self, authorization, orders_numbers):
        driver = authorization
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        order_feed_page = OrderFeedPage(driver)
        last_order = order_feed_page.get_user_order(orders_numbers)
        order_in_progress = order_feed_page.get_user_order_in_progress()
        assert last_order == order_in_progress
