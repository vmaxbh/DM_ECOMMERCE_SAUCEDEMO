from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")

    def fill_checkout_info(self, first_name, last_name, postal_code):
        self.send_keys(*self.first_name_field, first_name)
        self.send_keys(*self.last_name_field, last_name)
        self.send_keys(*self.postal_code_field, postal_code)

    def click_continue(self):
        self.click_element(*self.continue_button)

    def click_finish(self):
        self.click_element(*self.finish_button)
