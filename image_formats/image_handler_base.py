# image_formats/image_handler_base.py (ACTUALIZADO)
from PIL import Image
import os

class ImageHandlerBase:
    """
    Clase base para el manejo de formatos de imagen.
    Define la interfaz que todos los handlers de imagen deben implementar.
    """

    def load_image(self, filepath: str) -> Image.Image:
        """
        Carga una imagen desde la ruta especificada.
        Debe ser implementado por las clases hijas.
        """
        raise NotImplementedError("El método 'load_image' debe ser implementado por la subclase.")

    def compress_image(self, image: Image.Image, output_path: str, quality: int = None, algorithm_name: str = None):
        """
        Comprime y guarda una imagen en la ruta de salida,
        manejando la posible conversión de formato y aplicando el algoritmo deseado.
        Debe ser implementado por las clases hijas.
        """
        raise NotImplementedError("El método 'compress_image' debe ser implementado por la subclase.")

    def get_supported_extensions(self) -> list[str]:
        """
        Devuelve una lista de extensiones de archivo soportadas por este handler.
        Debe ser implementado por las clases hijas.
        """
        raise NotImplementedError("El método 'get_supported_extensions' debe ser implementado por la subclase.")

    @staticmethod
    def _convert_and_save(image: Image.Image, output_path: str, format: str, quality: int = None, algorithm_name: str = None):
        """
        Método estático auxiliar para manejar la conversión y el guardado.
        Puede ser utilizado por las clases hijas para evitar duplicación.
        """
        _, ext = os.path.splitext(output_path.lower())

        save_params = {}

        if format.upper() == 'JPEG':
            if image.mode == 'RGBA': # Convertir RGBA a RGB si es JPEG
                image = image.convert('RGB')
            save_params['quality'] = quality if quality is not None else 85
            save_params['optimize'] = True
        elif format.upper() == 'PNG':
            save_params['optimize'] = True
        elif format.upper() == 'WEBP':
            # WebP soporta tanto compresión con pérdida como sin pérdida
            # Si algorithm_name es 'lossless', Pillow usará compresión sin pérdida
            if algorithm_name and algorithm_name.lower() == 'lossless':
                save_params['lossless'] = True
                # La calidad en modo lossless de WebP afecta el esfuerzo de compresión (0-100)
                save_params['quality'] = quality if quality is not None else 80 # default para lossless
            else: # Por defecto, WebP usa compresión con pérdida
                save_params['quality'] = quality if quality is not None else 85
                save_params['optimize'] = True
            
            # WebP también soporta transparencia (RGBA), si la imagen original la tiene, Pillow la conservará.
            if image.mode not in ['RGB', 'RGBA']:
                # Convertir a RGBA para mejor compatibilidad con WebP si no es ya RGB/RGBA
                image = image.convert('RGBA')

        try:
            image.save(output_path, format=format, **save_params)
            print(f"Imagen guardada como {format} en: {output_path}")
        except Exception as e:
            raise Exception(f"Error al guardar la imagen como {format}: {e}")