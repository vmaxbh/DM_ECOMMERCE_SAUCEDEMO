import os
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BaseClass:
    def __init__(self, driver):
        self.driver = driver

    def capture_screenshot(self, cenario, id_test, step_name):
        """Captura o print da tela e salva com o nome do step"""
        # Define o diretório onde as capturas de tela serão salvas
        folder_name = os.path.join("Screenshot", cenario, id_test)
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Cria o caminho do arquivo baseado no step_name
        timestamp = time.strftime(
            "%Y%m%d_%H%M%S"
        )  # Adiciona timestamp para evitar sobrescrita
        screenshot_path = os.path.join(folder_name, f"{step_name}_{timestamp}.png")

        # Captura a tela
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot salva em: {screenshot_path}")

    def get_element(self, xpath: str, timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    def get_element_visibility(self, xpath: str, timeout=10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

    def get_element_clickable(self, xpath: str, timeout=10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )

    def get_element_presence(self, xpath: str, timeout=10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )

    def scroll_to_element_webelement(self, element: WebElement):
        ActionChains(self.driver).scroll_to_element(element).perform()

    def scroll_to_element(self, xpath: str):
        element = self.get_element_presence(xpath)
        self.scroll_to_element_webelement(element)


