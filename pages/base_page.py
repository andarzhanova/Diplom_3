from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains


class BaselPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(locator))

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    def get_current_url(self):
        current_url = self.driver.current_url
        return current_url

    def wait_for_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))

    def get_attribute_value(self, locator, attribute):
        elm = self.driver.find_element(*locator)
        return elm.get_attribute(attribute)

    def get_actually_text(self, locator):
        actually_text = self.driver.find_element(*locator).text
        return actually_text

    def element_displayed(self, locator):
        elm = self.driver.find_element(*locator)
        return elm.is_displayed()

    def drag_and_drop_on_element(self, locator_one, locator_two):
        draggable = self.driver.find_element(*locator_one)
        droppable = self.driver.find_element(*locator_two)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable, droppable).perform()

    def wait_for_invisibility_of_element(self, locator):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for_text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.text_to_be_present_in_element(locator, text))

    def click_on_element_js(self, locator):
        elm = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", elm)
