import allure
import requests
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BaselPage
from data.api_constants import ApiConstants


class OrderFeedPage(BaselPage):
    ORDER_FEED_URL = "https://stellarburgers.nomoreparties.site/feed"  # URL страницы "Лента заказов"

    @allure.step('Проверяем переход на страницу Ленты заказов')
    def check_switch_on_order_feed(self):
        self.wait_for_visibility_of_element(OrderFeedLocators.ORDER_FEED_HEADER)
        current_url = self.get_current_url()
        assert current_url == self.ORDER_FEED_URL

    @allure.step('Нажимаем кнопку «Конструктор»')
    def click_constructor_button(self):
        self.click_on_element(OrderFeedLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликаем на заказ')
    def click_on_order(self):
        self.wait_for_element_to_be_clickable(OrderFeedLocators.ORDER)
        self.click_on_element(OrderFeedLocators.ORDER)

    @allure.step('Проверяем, что появилось всплывающее окно с деталями')
    def check_show_window_with_details(self):
        self.wait_for_visibility_of_element(OrderFeedLocators.POP_UP_WINDOW)
        assert self.element_displayed(OrderFeedLocators.POP_UP_WINDOW)

    @allure.step('Получаем номера всех заказов в Ленте заказов')
    def get_orders_numbers(self, user_orders):
        last_order = '0' + str(user_orders[-1])
        self.wait_for_text_to_be_present_in_element(OrderFeedLocators.NUMBER_IN_PROGRESS, last_order)
        text = '#0' + str(user_orders[-1])
        self.wait_for_text_to_be_present_in_element(OrderFeedLocators.LAST_ORDER, text)
        all_elements = self.find_elements(OrderFeedLocators.ORDER_NUMBERS)
        return [elm.text.strip('#0') for elm in all_elements]

    @allure.step('Проверяем, что заказы пользователя отображаются в Ленте заказов')
    def check_user_orders_in_feed_orders(self, user_orders):
        feed_orders = self.get_orders_numbers(user_orders)
        for order_number in user_orders:
            assert str(order_number) in feed_orders, 'Заказы пользователя не отображаются в Ленте заказов'

    @allure.step('Получаем значение счетчика заказов')
    def get_counter_value(self, counter):
        self.wait_for_visibility_of_element(OrderFeedLocators.ORDER_FEED_HEADER)
        return self.get_actually_text(counter)

    @allure.step('Создаём новый заказ')
    def create_order(self, user_token):
        token = user_token
        payload = ApiConstants.INGREDIENTS
        requests.post(ApiConstants.ORDER, headers={'Authorization': token}, data=payload)

    @allure.step('Проверяем, что значение счетчика увеличилось после создания нового заказа')
    def check_increasing_counter(self, counter, user_token):
        prev_counter_value = self.get_counter_value(counter)
        self.create_order(user_token)
        current_counter_value = self.get_counter_value(counter)
        assert current_counter_value > prev_counter_value

    @allure.step('Проверяем, что номер заказа появился в разделе "В работе"')
    def check_user_order_in_progress(self, orders_numbers):
        last_order = '0' + str(orders_numbers[-1])
        self.wait_for_text_to_be_present_in_element(OrderFeedLocators.NUMBER_IN_PROGRESS, last_order)
        order_in_progress = self.get_actually_text(OrderFeedLocators.NUMBER_IN_PROGRESS)
        assert last_order == order_in_progress
