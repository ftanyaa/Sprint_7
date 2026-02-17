from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def open(self):
        self._driver.get("https://qa-scooter.praktikum-services.ru/")

    def click_top_order(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)

    def click_bottom_order(self):
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)
