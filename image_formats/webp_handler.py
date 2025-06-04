# image_formats/webp_handler.py
from PIL import Image
import os
from .image_handler_base import ImageHandlerBase

class WebPImageHandler(ImageHandlerBase):
    """
    Handler para imágenes WebP.
    """
    def load_image(self, filepath: str) -> Image.Image:
        """Carga una imagen WebP."""
        try:
            return Image.open(filepath)
        except FileNotFoundError:
            raise FileNotFoundError(f"No se encontró el archivo: {filepath}")
        except Exception as e:
            raise Exception(f"Error al cargar la imagen WebP: {e}")

    def compress_image(self, image: Image.Image, output_path: str, quality: int = None, algorithm_name: str = None):
        """
        Comprime y guarda una imagen como WebP (o convierte a otro formato si la extensión es diferente),
        considerando el algoritmo de compresión.
        """
        _, output_extension = os.path.splitext(output_path.lower())
        
        if output_extension == '.webp':
            self._convert_and_save(image, output_path, 'WEBP', quality=quality, algorithm_name=algorithm_name)
        elif output_extension == '.png':
            self._convert_and_save(image, output_path, 'PNG', quality=quality, algorithm_name=algorithm_name)
        elif output_extension == '.jpg' or output_extension == '.jpeg':
            self._convert_and_save(image, output_path, 'JPEG', quality=quality, algorithm_name=algorithm_name)
        else:
            raise ValueError(f"Formato de salida no soportado para WebP Handler: {output_extension}")

    def get_supported_extensions(self) -> list[str]:
        """Devuelve una lista de las extensiones soportadas por este handler."""
        return ['.webp']