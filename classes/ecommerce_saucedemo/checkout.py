from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from classes.base_class import BaseClass
from decorators.decorators import retry
import time




class TestCheckout(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    @retry(max_attempts=3)
    def fill_checkout_your_information(self, first_name, last_name, street_and_house_number, apartment_number, city, state, postal_code):
        self.get_element("//input[@id='order_ship_address_attributes_firstname']", timeout=16).send_keys(first_name)
        self.get_element("//input[@id='order_ship_address_attributes_lastname']", timeout=16).send_keys(last_name)
        element = self.get_element("//input[@id='order_ship_address_attributes_address1']")


    @retry(max_attempts=3)
    def registration_checkout(self):
        country = "Brazil"
        first_name = "Maxwell"
        last_name = "Viana"
        street_and_house_number = "Rua Um numero, 55"
        apartment_number = "55"
        city = "Belo Horizonte"
        state = "Minas Gerais"
        postal_code = "30710520"
        self.fill_checkout_your_information(country, first_name, last_name, street_and_house_number, apartment_number, city, state, postal_code)

    @retry(max_attempts=3)
    def click_btn_checkout(self):
        self.get_element_clickable("//button[@id='checkout']").click()
        time.sleep(10)




