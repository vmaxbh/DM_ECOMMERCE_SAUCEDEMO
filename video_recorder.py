from datetime import datetime
import os
from selenium import webdriver
from PIL import Image
import io
from moviepy.editor import ImageSequenceClip

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

        # Salva a imagem temporariamente
        temp_path = os.path.join(self.output_dir, f"temp_{len(self.frames)}.png")
        image.save(temp_path)

        self.frames.append(temp_path)

    def stop_recording(self, test_name="test"):
        """Para a gravação e salva o vídeo em MP4"""
        if not self.recording:
            return

        self.recording = False

        if not self.frames:
            print("Nenhum frame capturado para salvar o vídeo.")
            return

        # Gera o nome do arquivo com timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{test_name}_{timestamp}.mp4"
        output_path = os.path.join(self.output_dir, filename)

        try:
            # Cria o vídeo a partir das imagens
            clip = ImageSequenceClip(self.frames, fps=10)
            clip.write_videofile(output_path, codec='libx264')
            print(f"Vídeo salvo em: {output_path}")
        finally:
            # Limpa os arquivos temporários
            for frame_path in self.frames:
                if os.path.exists(frame_path):
                    os.remove(frame_path)
            self.frames = []
