import pytest
from tests.id01_compra_standard.id01_login import Teste01LoginStandard
from tests.id01_compra_standard.id02_product import Teste02Products
from tests.id01_compra_standard.id03_checkout import Teste03Checkout
from tests.id01_compra_standard.id04_complete_purchase import Teste04CompletePurchase


class TestExecutionCompraStandard:
    def test_execution(self):
        Teste01LoginStandard().__init__()
        Teste02Products().__init__()
        Teste03Checkout().__init__()
        Teste04CompletePurchase().__init__()
