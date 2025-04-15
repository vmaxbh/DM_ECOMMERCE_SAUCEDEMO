import pytest
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    """Função para deletar a pasta Screenshot antes e após os testes"""
    delete_screenshot_folder()  # Exclui a pasta Screenshot no início
    yield
    print("Testes finalizados.")


@pytest.fixture(scope="session")
def browser():
    """Fixture para inicializar o navegador"""
    chrome_options = Options()

    headless_value = os.getenv("HEADLESS", "true")
    print(f"Valor da variável HEADLESS: {headless_value}")

    if headless_value.lower() != "false":
        chrome_options.add_argument("--headless")  # Modo headless

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    )

    # Maximiza a janela do navegador
    driver.maximize_window()

    yield driver
    driver.quit()


def delete_screenshot_folder():
    """Verifica se a pasta Screenshot existe e apaga ela se existir"""
    folder_name = "Screenshot"

    # Verifica se a pasta Screenshot existe
    if os.path.exists(folder_name):
        # Apaga a pasta Screenshot e todo o seu conteúdo
        shutil.rmtree(folder_name)
        print(f"A pasta {folder_name} foi apagada com sucesso.")
    else:
        print(f"A pasta {folder_name} não existe.")
