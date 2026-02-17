from selenium.webdriver.common.by import By

class MainPageLocators:
    TOP_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle')]")
