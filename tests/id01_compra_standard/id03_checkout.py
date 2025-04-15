import pytest
from selenium import webdriver
from classes.ecommerce_saucedemo.login_class import LoginPage
from classes.ecommerce_saucedemo.credencials_class import Credenciais
from classes.base_class import BaseClass
from classes.ecommerce_saucedemo.navigate_class import TestNavigate
from classes.ecommerce_saucedemo.checkout import TestCheckout
import time

cenario = "id01_Compra_Standard"
id_test = "test_id03"


class Teste03Checkout:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.driver = browser
        self.login_page = LoginPage(self.driver)
        self.base = BaseClass(self.driver)
        self.navigate = TestNavigate(self.driver)
        self.checkout = TestCheckout(self.driver)

    def test_Checkout_Standard(self):
        step = "step_1"
        self.checkout.click_btn_checkout()
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_2"
        self.checkout.registration_checkout()
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_3"
        self.checkout.click_btn_continue()
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_4"
        self.checkout.validation_informations_checkout()
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
