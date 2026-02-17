from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage(BasePage):
    def fill_form(self, name, surname, address, metro, phone):
        self.input_text(OrderPageLocators.NAME_INPUT, name)
        self.input_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.input_text(OrderPageLocators.ADDRESS_INPUT, address)
        metro_input = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.METRO_INPUT)
        )
        metro_input.send_keys(metro)
        metro_option = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.METRO_OPTION)
        )
        metro_option.click()
        self.input_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)
