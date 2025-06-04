# image_formats/jpg_handler.py
from PIL import Image
import os
from .image_handler_base import ImageHandlerBase

class JPGImageHandler(ImageHandlerBase):
    """
    Handler para imágenes JPG.
    """
    def load_image(self, filepath: str) -> Image.Image:
        """Carga una imagen JPG."""
        try:
            return Image.open(filepath)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {filepath}")
        except Exception as e:
            raise Exception(f"Error al cargar la imagen JPG: {e}")

    def compress_image(self, image: Image.Image, output_path: str, quality: int = 85, algorithm_name: str = None):
        """
        Comprime y guarda una imagen como JPG (o convierte a otro formato si la extensión es diferente),
        considerando el algoritmo de compresión.
        """
        _, output_extension = os.path.splitext(output_path.lower())
        
        if output_extension == '.jpg' or output_extension == '.jpeg':
            self._convert_and_save(image, output_path, 'JPEG', quality=quality, algorithm_name=algorithm_name)
        elif output_extension == '.png':
            self._convert_and_save(image, output_path, 'PNG', quality=quality, algorithm_name=algorithm_name)
        elif output_extension == '.webp': # AÑADIR ESTA LÍNEA
            self._convert_and_save(image, output_path, 'WEBP', quality=quality, algorithm_name=algorithm_name) # Y ESTA LÍNEA
        else:
            raise ValueError(f"Formato de salida no soportado para JPG Handler: {output_extension}")
        
    def get_supported_extensions(self) -> list[str]:
        """Devuelve una lista de las extensiones soportadas por este handler."""
        return ['.jpg', '.jpeg']