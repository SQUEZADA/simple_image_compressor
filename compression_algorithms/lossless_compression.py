# compression_algorithms/lossless_compression.py
from PIL import Image
from .compression_algorithm_base import CompressionAlgorithmBase # Importar la clase base

class LosslessCompression(CompressionAlgorithmBase):
    """
    Algoritmo de compresión sin pérdida (típicamente PNG).
    """
    def compress(self, image: Image.Image, output_path: str, **kwargs):
        """Comprime una imagen sin pérdida (PNG)."""
        # Asumimos que la conversión a PNG se hará a través del ImageHandler si es necesario
        image.save(output_path, 'PNG', optimize=True)
        print(f"Compresión sin pérdida aplicada y guardada en: {output_path}")

    def get_name(self) -> str:
        """Devuelve el nombre de este algoritmo."""
        return "lossless"