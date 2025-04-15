import pytest
import sys
import os

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.id01_compra_standard.id01_login import Teste01LoginStandard
from tests.id01_compra_standard.id02_product import Teste02Products
from tests.id01_compra_standard.id03_checkout import Teste03Checkout
from tests.id01_compra_standard.id04_complete_purchase import Teste04CompletePurchase
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage


class TestExecutionCompraStandard:
    def test_execution(self):
        Teste01LoginStandard().__init__()
        Teste02Products().__init__()
        Teste03Checkout().__init__()
        Teste04CompletePurchase().__init__()


@pytest.mark.usefixtures("browser", "video_recorder")
class TestCompraStandard:
    def test_compra_padrao(self, browser, video_recorder):
        # Login
        login_page = LoginPage(browser)
        login_page.navigate_to_login()
        login_page.login("standard_user", "secret_sauce")
        video_recorder.capture_frame()

        # Navegação e seleção de produtos
        inventory_page = InventoryPage(browser)
        inventory_page.click_product("Sauce Labs Backpack")
        video_recorder.capture_frame()

        product_page = ProductPage(browser)
        product_page.add_to_cart()
        product_page.click_back_to_products()
        video_recorder.capture_frame()

        inventory_page.click_product("Sauce Labs Bike Light")
        video_recorder.capture_frame()
        product_page.add_to_cart()
        product_page.click_back_to_products()
        video_recorder.capture_frame()

        # Carrinho
        inventory_page.click_cart()
        video_recorder.capture_frame()
        cart_page = CartPage(browser)
        cart_page.click_checkout()
        video_recorder.capture_frame()

        # Checkout
        checkout_page = CheckoutPage(browser)
        checkout_page.fill_checkout_info("Maxwell", "Teste", "12345")
        video_recorder.capture_frame()
        checkout_page.click_continue()
        video_recorder.capture_frame()
        checkout_page.click_finish()
        video_recorder.capture_frame()
