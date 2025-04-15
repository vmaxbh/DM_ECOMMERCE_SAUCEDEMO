import pytest
import os
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from video_recorder import VideoRecorder


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

    # Configurações para modo anônimo e outras opções de segurança
    chrome_options.add_argument("--incognito")  # Modo anônimo
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-notifications")  # Desabilita notificações
    chrome_options.add_argument(
        "--disable-popup-blocking"
    )  # Permite popups se necessário

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


def pytest_html_report_title(report):
    """Hook para configurar o título do relatório HTML"""
    report.title = "DM- Teste de Capacitação Técnica - Maxwell e-commerce Saucedemo"


@pytest.fixture(scope="function")
def video_recorder(browser):
    """Fixture para gerenciar a gravação de vídeo durante os testes"""
    recorder = VideoRecorder(browser)
    return recorder


@pytest.fixture(autouse=True)
def record_video(request, video_recorder):
    """Fixture que inicia e para a gravação de vídeo automaticamente"""
    if os.getenv("HEADLESS", "true").lower() == "true":
        video_recorder.start_recording()
        yield
        video_recorder.stop_recording(request.node.name)
    else:
        yield
