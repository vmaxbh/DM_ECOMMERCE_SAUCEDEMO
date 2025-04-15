from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from classes.base_class import BaseClass
from decorators.decorators import retry
from faker import Faker
import time


class TestCheckout(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.fake = Faker("pt_BR")  # Inicializa o Faker com localização brasileira

    @retry(max_attempts=3)
    def fill_checkout_your_information(self, first_name, last_name, zip_postal_code):
        self.get_element("//input[@id='first-name']", timeout=16).send_keys(first_name)
        self.get_element("//input[@id='last-name']", timeout=16).send_keys(last_name)
        self.get_element("//input[@id='postal-code']", timeout=16).send_keys(
            zip_postal_code
        )

    @retry(max_attempts=3)
    def registration_checkout(self):
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
        zip_postal_code = self.fake.postcode()
        self.fill_checkout_your_information(first_name, last_name, zip_postal_code)

    @retry(max_attempts=3)
    def click_btn_checkout(self):
        self.get_element_clickable("//button[@id='checkout']").click()
        self.get_element_visibility(
            "//span[contains(text(), 'Checkout: Your Information')]", timeout=16
        )

    @retry(max_attempts=3)
    def click_btn_continue(self):
        self.get_element_clickable("//input[@id='continue']").click()
        self.get_element_visibility(
            "//span[contains(text(), 'Checkout: Overview')]", timeout=16
        )

    def validation_informations_checkout(self):
        self.get_element_visibility("//div[@class='cart_item_label']", timeout=16)
        self.get_element_visibility("//div[@class='summary_value_label']", timeout=16)
        self.get_element_visibility("//div[@class='summary_total_label']", timeout=16)
        self.get_element_visibility("//div[@class='summary_tax_label']", timeout=16)
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).perform()

    def validation_complete_purchase(self):
        self.get_element_visibility(
            "//h2[contains(text(), 'Thank you for your order!')]", timeout=16
        )
