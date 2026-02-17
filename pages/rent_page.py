from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators.rent_page_locators import RentPageLocators

class RentPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_rent_form(self, date, period, color):
        date_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RentPageLocators.DATE_INPUT)
        )
        date_input.click()
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RentPageLocators.PERIOD_DROPDOWN)
        )
        dropdown.click()
        if period == "сутки":
            self.driver.find_element(*RentPageLocators.PERIOD_OPTION_DAY).click()
        else:
            self.driver.find_element(*RentPageLocators.PERIOD_OPTION_FOUR_DAYS).click()

        if color == "black":
            self.driver.find_element(*RentPageLocators.COLOR_BLACK).click()
        else:
            self.driver.find_element(*RentPageLocators.COLOR_GREY).click()

    def confirm_order(self):
        self.click(RentPageLocators.CONFIRM_BUTTON)
        self.click(RentPageLocators.FINAL_CONFIRM_BUTTON)

    def is_order_created(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RentPageLocators.ORDER_MODAL_HEADER)
        ).is_displayed()

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
