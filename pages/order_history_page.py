import allure
from locators.order_history_locators import OrderHistoryLocators
from pages.base_page import BaselPage
from data.urls_constants import UrlsConstants


class OrderHistoryPage(BaselPage):
    @allure.step('Проверяем переход на страницу История заказов')
    def check_switch_on_order_history(self):
        self.wait_for_visibility_of_element(OrderHistoryLocators.ENABLED_ORDER_HISTORY_BUTTON)
        current_url = self.get_current_url()
        assert current_url == UrlsConstants.ORDER_HISTORY_URL

    @allure.step('Нажимаем кнопку «Выход»')
    def click_log_out_button(self):
        self.wait_for_element_to_be_clickable(OrderHistoryLocators.EXIT_BUTTON)
        self.click_on_element(OrderHistoryLocators.EXIT_BUTTON)
