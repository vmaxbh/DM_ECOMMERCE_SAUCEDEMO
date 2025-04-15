import pytest
from selenium import webdriver
from classes.ecommerce_saucedemo.login_class import LoginPage
from classes.ecommerce_saucedemo.checkout import TestCheckout
from classes.base_class import BaseClass


cenario = "id01_Compra_Standard"
id_test = "test_id04"


class Teste04CompletePurchase:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.driver = browser
        self.base = BaseClass(self.driver)
        self.checkout = TestCheckout(self.driver)

    def test_Complete_Purchase(self):
        step = "step_1"
        self.base.get_element_clickable("//button[@id='finish']").click()
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)
        step = "step_2"
        self.checkout.validation_complete_purchase()
