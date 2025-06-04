# compression_algorithms/palette_reduction_compression.py
from PIL import Image
from .compression_algorithm_base import CompressionAlgorithmBase

class PaletteReductionCompression(CompressionAlgorithmBase):
    """
    Algoritmo de compresión que reduce el número de colores en la imagen.
    Útil para PNGs o para preparar imágenes para formatos con paleta limitada.
    """
    def compress(self, image: Image.Image, output_path: str, **kwargs):
        """
        Aplica la reducción de paleta a la imagen.
        El número de colores se puede especificar con 'colors'.
        """
        num_colors = kwargs.get('colors', 256) # Por defecto a 256 colores
        dither = kwargs.get('dither', True) # Aplicar dithering por defecto

        try:
            # Convierte la imagen al modo 'P' (paleta) con el número especificado de colores.
            # `dither=Image.Dither.FLOYDSTEINBERG` es el valor por defecto para True.
            # Si dither es False, se usa Image.FLOYDSTEINBERG=0, que no aplica dithering.
            quantized_image = image.quantize(colors=num_colors, dither=dither)
            
            # NOTA IMPORTANTE: Este algoritmo *modifica* la imagen en memoria.
            # El handler de imagen luego tomará esta imagen ya modificada y la guardará.
            
            print(f"Aplicada reducción de paleta a {num_colors} colores.")
            
            # Devolvemos la imagen cuantificada. El handler la guardará.
            return quantized_image
        except Exception as e:
            raise Exception(f"Error durante la compresión con reducción de paleta: {e}")

    def get_name(self) -> str:
        """Devuelve el nombre de este algoritmo."""
        return "palette_reduction"