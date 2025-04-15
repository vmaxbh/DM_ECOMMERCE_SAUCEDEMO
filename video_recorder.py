from datetime import datetime
import os
from selenium import webdriver
from PIL import Image
import io

class VideoRecorder:
    def __init__(self, driver: webdriver.Chrome, output_dir="video"):
        self.driver = driver
        self.output_dir = output_dir
        self.frames = []
        self.recording = False

        # Cria o diretório de saída se não existir
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def start_recording(self):
        """Inicia a gravação do vídeo"""
        self.recording = True
        self.frames = []
        print("Iniciando gravação do vídeo...")

    def capture_frame(self):
        """Captura um frame da tela atual"""
        if not self.recording:
            return

        # Captura a screenshot
        screenshot = self.driver.get_screenshot_as_png()

        # Converte para imagem PIL
        image = Image.open(io.BytesIO(screenshot))

        # Redimensiona a imagem para um tamanho menor (opcional)
        image = image.resize((800, 600), Image.Resampling.LANCZOS)

        self.frames.append(image)

    def stop_recording(self, test_name="test"):
        """Para a gravação e salva o vídeo em GIF"""
        if not self.recording:
            return

        self.recording = False

        if not self.frames:
            print("Nenhum frame capturado para salvar o vídeo.")
            return

        # Gera o nome do arquivo com timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.gif"
        output_path = os.path.join(self.output_dir, filename)

        try:
            # Salva o GIF animado
            self.frames[0].save(
                output_path,
                save_all=True,
                append_images=self.frames[1:],
                optimize=True,
                duration=100,  # 100ms entre frames = 10fps
                loop=0
            )
            print(f"Vídeo salvo em: {output_path}")
        finally:
            # Limpa os frames
            self.frames = []
