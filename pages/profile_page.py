import allure
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage
from data.urls_constants import UrlsConstants


class ProfilePage(BasePage):
    @allure.step('Проверяем переход на страницу профиля')
    def check_switch_on_profile(self):
        self.wait_for_visibility_of_element(ProfilePageLocators.PROFILE_BUTTON)
        current_url = self.get_current_url()
        assert current_url == UrlsConstants.PROFILE_URL

    @allure.step('Нажимаем кнопку «История заказов»')
    def click_order_history_button(self):
        self.wait_for_element_to_be_clickable(ProfilePageLocators.ORDER_HISTORY_BUTTON)
        self.click_on_element(ProfilePageLocators.ORDER_HISTORY_BUTTON)
