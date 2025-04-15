from selenium.webdriver.common.keys import Keys
from classes.base_class import BaseClass
from decorators.decorators import retry


class TestNavigate(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    @retry(max_attempts=3)
    def navigate_and_select_product(self, product_name):
        self.scroll_to_element(f"//button[@id='add-to-cart-{product_name}']")
        self.get_element_clickable(
            f"//button[@id='add-to-cart-{product_name}']"
        ).click()
