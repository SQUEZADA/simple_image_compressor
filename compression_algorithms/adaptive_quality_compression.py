# compression_algorithms/adaptive_quality_compression.py
from PIL import Image
from .compression_algorithm_base import CompressionAlgorithmBase

class AdaptiveQualityCompression(CompressionAlgorithmBase):
    """
    Algoritmo que simula una compresión de calidad adaptativa.
    En la implementación actual, simplemente usa la calidad proporcionada,
    pero puede extenderse para ajustar la calidad dinámicamente.
    """
    def compress(self, image: Image.Image, output_path: str, **kwargs):
        """
        Este método no guarda la imagen directamente, sino que
        su presencia indica que este algoritmo está siendo usado.
        La lógica de guardado y aplicación de calidad se maneja en el ImageHandler
        basado en el 'algorithm_name' y el 'quality' pasados.
        """
        # Aquí es donde pondrías lógica para, por ejemplo, analizar la imagen
        # y decidir una calidad óptima antes de pasarla al handler.
        # Por ejemplo:
        # if image.width > 2000:
        #     recommended_quality = kwargs.get('quality', 85) - 10
        # else:
        #     recommended_quality = kwargs.get('quality', 85)

        # En este modelo, el `compressor.py` pasa el `algorithm_name` al handler,
        # y el handler utiliza la `quality` y el `algorithm_name` para la llamada final a `_convert_and_save`.
        # Así que este método `compress` aquí es más un marcador y podría ser un lugar
        # para futuras pre-procesamientos o ajustes de parámetros.
        print(f"Preparando compresión con estrategia '{self.get_name()}'...")


    def get_name(self) -> str:
        """Devuelve el nombre de este algoritmo."""
        return "adaptive_quality"