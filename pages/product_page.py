from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button = (By.ID, "add-to-cart")
        self.back_to_products_button = (By.ID, "back-to-products")

    def add_to_cart(self):
        self.click_element(*self.add_to_cart_button)

    def click_back_to_products(self):
        self.click_element(*self.back_to_products_button)
