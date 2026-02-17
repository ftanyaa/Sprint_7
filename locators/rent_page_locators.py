from selenium.webdriver.common.by import By

class RentPageLocators:
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-root")
    PERIOD_OPTION_DAY = (By.XPATH, "//div[text()='сутки']")
    PERIOD_OPTION_FOUR_DAYS = (By.XPATH, "//div[text()='четверо суток']")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    FINAL_CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_MODAL_HEADER = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
