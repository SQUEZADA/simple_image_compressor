# compression_algorithms/compression_algorithm_base.py
from PIL import Image

class CompressionAlgorithmBase:
    """
    Clase base para los algoritmos de compresión.
    Define la interfaz que todos los algoritmos deben implementar.
    """

    def compress(self, image: Image.Image, output_path: str, **kwargs):
        """
        Aplica el algoritmo de compresión a la imagen y la guarda.
        Debe ser implementado por las clases hijas.
        Los kwargs permiten pasar parámetros específicos del algoritmo (e.g., quality).
        """
        raise NotImplementedError("El método 'compress' debe ser implementado por la subclase.")

    def get_name(self) -> str:
        """
        Devuelve el nombre del algoritmo.
        Debe ser implementado por las clases hijas.
        """
        raise NotImplementedError("El método 'get_name' debe ser implementado por la subclase.")