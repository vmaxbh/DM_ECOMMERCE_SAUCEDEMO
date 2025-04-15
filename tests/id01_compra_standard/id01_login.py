import pytest
from selenium import webdriver
from classes.ecommerce_saucedemo.login_class import LoginPage
from classes.ecommerce_saucedemo.credencials_class import Credenciais
from classes.base_class import BaseClass

cenario = "id01_Compra_Standard"
id_test = "test_id01"


class Teste01LoginStandard:
    @pytest.fixture(autouse=True)
    def setup_method(self, browser):
        """Inicializa o driver e a página de login."""
        self.driver = browser
        self.login_page = LoginPage(self.driver)
        self.base = BaseClass(self.driver)

    def test_login_sucesso(self):
        """Testa o login bem-sucedido."""
        step = "step_1"
        self.login_page.login(Credenciais.USUARIO_CORRETO, Credenciais.SENHA_CORRETA)
        self.base.capture_screenshot(cenario, f"Evidencias {id_test}", step)



