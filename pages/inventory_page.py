from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def click_product(self, product_name):
        product_locator = (By.XPATH, f"//div[text()='{product_name}']")
        self.click_element(*product_locator)

    def click_cart(self):
        self.click_element(*self.cart_button)
