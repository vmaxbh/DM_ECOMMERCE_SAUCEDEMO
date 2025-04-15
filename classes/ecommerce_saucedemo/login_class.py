from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from classes.base_class import BaseClass
import time


class LoginPage(BaseClass):
    def __init__(self, browser):
        super().__init__(browser)
        self.driver = browser
        self.username_field = "//input[@id='user-name']"
        self.password_field = "//input[@id='password']"
        self.login_button = "//input[@id='login-button']"

    def login(self, usuario, senha):
        self.driver.get("https://www.saucedemo.com/")
        self.get_element(self.username_field, timeout=20).send_keys(usuario)
        self.get_element(self.password_field, timeout=20).send_keys(senha)
        self.get_element_clickable(self.login_button, timeout=20).click()
        self.verificar_login_sucesso()
        print(f"Login realizado com usuário: {usuario}")

    def verificar_login_sucesso(self):
        self.get_element_visibility("//span[contains(text(), 'Products')]", timeout=20)
