import pytest
from selenium import webdriver
from classes.ecommerce_saucedemo.login_class import LoginPage
from classes.ecommerce_saucedemo.credencials_class import Credenciais
from classes.base_class import BaseClass
from classes.ecommerce_saucedemo.navigate_class import TestNavigate
from classes.ecommerce_saucedemo.checkout import TestCheckout
import time

cenario = "id01_Compra_Standard"
id_test = "test_id02"


class Teste02Products:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.driver = browser
        self.login_page = LoginPage(self.driver)
        self.base = BaseClass(self.driver)
        self.navigate = TestNavigate(self.driver)
        self.checkout = TestCheckout(self.driver)

    def test_Products(self):
        step = "step_1"
        self.navigate.navigate_and_select_product("sauce-labs-onesie")
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_2"
        self.navigate.navigate_and_select_product("test.allthethings()-t-shirt-(red)")
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_3"
        time.sleep(5)
        self.base.get_element_clickable(
            "//a[@class='shopping_cart_link']", timeout=20
        ).click()
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
