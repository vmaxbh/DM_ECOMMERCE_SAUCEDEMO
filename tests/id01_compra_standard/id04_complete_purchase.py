import pytest
from selenium import webdriver
from classes.ecommerce_saucedemo.login_class import LoginPage
from classes.ecommerce_saucedemo.credencials_class import Credenciais
from classes.base_class import BaseClass
from classes.ecommerce_saucedemo.navigate_class import TestNavigate
from classes.ecommerce_saucedemo.checkout import TestCheckout
import time

cenario = "id01_Compra_Standard"
id_test = "test_id05"


class Teste05CompletePurchase:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        self.driver = browser
        self.login_page = LoginPage(self.driver)
        self.base = BaseClass(self.driver)
        self.navigate = TestNavigate(self.driver)
        self.checkout = TestCheckout(self.driver)

    def test_Complete_Purchase(self):
        step = "step_4"
        time.sleep(3)
        self.base.get_element_visibility("//iframe[@title='Estrutura segura de checkout expresso']", timeout=10)
        self.base.enter_iframe("//iframe[@title='Estrutura segura de checkout expresso']")
        time.sleep(3)
        self.base.get_element_visibility("//iframe[contains(@src, 'GooglePay.html')]")
        self.base.enter_iframe("//iframe[contains(@src, 'GooglePay.html')]")
        time.sleep(3)
        self.checkout.click_complete_purchase()
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)

        # Sai dos iframes (volta para o contexto principal)
        self.base.exit_iframe()  # Sai do iframe do Google Pay
        self.base.exit_iframe()  # Sai do iframe do Stripe

        step = "step_5"
        self.checkout.click_pay_now()
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)


