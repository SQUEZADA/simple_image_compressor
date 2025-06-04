# compression_algorithms/lossy_compression.py
from PIL import Image
from .compression_algorithm_base import CompressionAlgorithmBase # Importar la clase base

class LossyCompression(CompressionAlgorithmBase):
    """
    Algoritmo de compresión con pérdida (típicamente JPG).
    """
    def compress(self, image: Image.Image, output_path: str, **kwargs):
        """Comprime una imagen con pérdida (JPG) usando el nivel de calidad."""
        quality = kwargs.get('quality', 85) # Obtener calidad o usar 85 por defecto
        # Asumimos que la conversión a JPG se hará a través del ImageHandler si es necesario
        image.save(output_path, 'JPEG', optimize=True, quality=quality)
        print(f"Compresión con pérdida aplicada y guardada en: {output_path} con calidad {quality}")

    def get_name(self) -> str:
        """Devuelve el nombre de este algoritmo."""
        return "lossy"