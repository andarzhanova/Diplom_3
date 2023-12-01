import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data.main_page_constants import MainPageConstants


class MainPage(BasePage):
    @allure.step('Нажимаем кнопку «Личный кабинет»')
    def click_personal_account_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Нажимаем кнопку «Лента Заказов»')
    def click_order_feed_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.ORDER_FEED_BUTTON)
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('Проверяем переход на главную страницу')
    def check_switch_on_main_page(self):
        self.wait_for_visibility_of_element(MainPageLocators.BURGER_HEADER)
        current_url = self.get_current_url()
        assert current_url == MainPageConstants.MAIN_PAGE_URL

    @allure.step('Кликаем на ингредиент')
    def click_on_ingredient(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BUN_INGREDIENT)
        self.click_on_element(MainPageLocators.BUN_INGREDIENT)

    @allure.step('Получаем значение счетчика ингредиента')
    def get_count_value(self):
        return self.get_actually_text(MainPageLocators.COUNTER)

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient(self):
        self.drag_and_drop_on_element(MainPageLocators.BUN_INGREDIENT, MainPageLocators.CONSTRUCTOR_BASKET)

    @allure.step('Нажимаем кнопку «Оформить заказ»')
    def click_checkout_button(self):
        self.click_on_element(MainPageLocators.CHECKOUT_BUTTON)

    @allure.step('Проверяем, что заказ оформлен и появился идентификатор заказа')
    def check_show_window_with_order_id(self):
        self.wait_for_visibility_of_element(MainPageLocators.ORDER_ID)
        actually_text = self.get_actually_text(MainPageLocators.ORDER_ID)
        assert actually_text == MainPageConstants.ORDER_ID
