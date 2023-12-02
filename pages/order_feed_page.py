import allure
import requests
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage
from data.api_constants import ApiConstants


class OrderFeedPage(BasePage):
    @allure.step('Проверяем переход на страницу Ленты заказов')
    def check_switch_on_order_feed(self):
        self.wait_for_visibility_of_element(OrderFeedLocators.ORDER_FEED_HEADER)
        return self.get_current_url()

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
        return self.element_displayed(OrderFeedLocators.POP_UP_WINDOW)

    @allure.step('Получаем номера всех заказов в Ленте заказов')
    def get_orders_numbers(self, user_orders):
        last_order = '0' + str(user_orders[-1])
        self.wait_for_text_to_be_present_in_element(OrderFeedLocators.NUMBER_IN_PROGRESS, last_order)
        text = '#0' + str(user_orders[-1])
        self.wait_for_text_to_be_present_in_element(OrderFeedLocators.LAST_ORDER, text)
        all_elements = self.find_elements(OrderFeedLocators.ORDER_NUMBERS)
        return [elm.text.strip('#0') for elm in all_elements]

    @allure.step('Получаем значение счетчика заказов')
    def get_counter_value(self, counter):
        self.wait_for_visibility_of_element(OrderFeedLocators.ORDER_FEED_HEADER)
        return self.get_actually_text(counter)

    @allure.step('Создаём новый заказ')
    def create_order(self, user_token):
        token = user_token
        payload = ApiConstants.INGREDIENTS
        requests.post(ApiConstants.ORDER, headers={'Authorization': token}, data=payload)

    @allure.step('Получаем номер заказа')
    def get_user_order(self, orders_numbers):
        last_order = '0' + str(orders_numbers[-1])
        self.wait_for_text_to_be_present_in_element(OrderFeedLocators.NUMBER_IN_PROGRESS, last_order)
        return last_order

    @allure.step('Получаем номер заказа в работе')
    def get_user_order_in_progress(self):
        return self.get_actually_text(OrderFeedLocators.NUMBER_IN_PROGRESS)
