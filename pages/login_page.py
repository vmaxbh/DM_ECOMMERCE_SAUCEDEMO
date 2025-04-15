from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def navigate_to_login(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.send_keys(*self.username_field, username)
        self.send_keys(*self.password_field, password)
        self.click_element(*self.login_button)
