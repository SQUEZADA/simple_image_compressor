# Simple Image Compressor
import os
import argparse
from PIL import UnidentifiedImageError

# --- IMPORTACIONES MANUALES DE HANDLERS DE IMAGEN ---
# Ensure these files exist in image_formats/ and contain the correct class definitions
from image_formats.png_handler import PNGImageHandler
from image_formats.jpg_handler import JPGImageHandler
from image_formats.webp_handler import WebPImageHandler
# ---------------------------------------------------

# --- IMPORTACIONES MANUALES DE ALGORITMOS DE COMPRESIÓN ---
# Ensure these files exist in compression_algorithms/ and contain the correct class definitions
from compression_algorithms.lossy_compression import LossyCompression
from compression_algorithms.lossless_compression import LosslessCompression
from compression_algorithms.adaptive_quality_compression import AdaptiveQualityCompression
from compression_algorithms.palette_reduction_compression import PaletteReductionCompression # NEW IMPORT
# --------------------------------------------------------

# --- Mapeo de extensiones a Handlers ---
IMAGE_HANDLERS = {
    '.png': PNGImageHandler(),
    '.jpg': JPGImageHandler(),
    '.jpeg': JPGImageHandler(), # JPG also supports .jpeg
    '.webp': WebPImageHandler(),
}

# --- Mapeo de nombres de algoritmo a Algoritmos ---
COMPRESSION_ALGORITHMS = {
    'lossy': LossyCompression(),
    'lossless': LosslessCompression(),
    'adaptive_quality': AdaptiveQualityCompression(),
    'palette_reduction': PaletteReductionCompression(), # NEW ALGORITHM MAPPING
}

def main():
    parser = argparse.ArgumentParser(description="Simple Image Compressor")
    parser.add_argument("input_path", help="Ruta de la imagen de entrada")
    parser.add_argument("output_path", help="Ruta para guardar la imagen comprimida")
    parser.add_argument("--quality", type=int, help="Nivel de calidad para compresión con pérdida (0-100). Default para JPG/WebP es 85. Para WebP lossless, afecta el esfuerzo.", default=85)
    parser.add_argument("--algorithm", type=str, help="Algoritmo de compresión a usar (lossy, lossless, adaptive_quality, palette_reduction).", default="lossy")
    parser.add_argument("--colors", type=int, help="Número de colores para el algoritmo 'palette_reduction'.", default=256) # NEW ARGUMENT

    args = parser.parse_args()

    input_path = args.input_path
    output_path = args.output_path
    quality = args.quality
    algorithm_name = args.algorithm
    colors = args.colors # Get the new 'colors' argument

    # 1. Validar la existencia del archivo de entrada
    if not os.path.exists(input_path):
        print(f"Error: El archivo de entrada '{input_path}' no existe.")
        return

    # 2. Seleccionar el handler de imagen adecuado (sin carga dinámica)
    _, input_extension = os.path.splitext(input_path.lower())
    image_handler = IMAGE_HANDLERS.get(input_extension)

    # 3. Seleccionar el algoritmo de compresión (sin carga dinámica)
    compression_algorithm_instance = COMPRESSION_ALGORITHMS.get(algorithm_name.lower())

    if not image_handler:
        supported_exts = ", ".join(IMAGE_HANDLERS.keys())
        print(f"Error: Formato de imagen no soportado para '{input_path}'. Extensiones soportadas: {supported_exts}")
        return

    if not compression_algorithm_instance:
        supported_algs = ", ".join(COMPRESSION_ALGORITHMS.keys())
        print(f"Error: Algoritmo de compresión '{algorithm_name}' no encontrado. Algoritmos soportados: {supported_algs}")
        return

    try:
        print(f"Cargando imagen: '{input_path}' usando {type(image_handler).__name__}...")
        img = image_handler.load_image(input_path)

        print(f"Aplicando algoritmo: '{compression_algorithm_instance.get_name()}'...")
        
        # Pass additional parameters relevant to the algorithm
        algorithm_kwargs = {'quality': quality}
        if algorithm_name.lower() == 'palette_reduction':
            algorithm_kwargs['colors'] = colors
            
        # The algorithm can process the image in memory if needed
        # For palette_reduction, it modifies the image directly.
        modified_img = compression_algorithm_instance.compress(img, output_path, **algorithm_kwargs) 
        if modified_img is not None: # If the algorithm returns a modified image
            img = modified_img

        # The ImageHandler is responsible for saving the image,
        # handling the format conversion and applying the quality/algorithm hints.
        image_handler.compress_image(img, output_path, quality=quality, algorithm_name=algorithm_name)
        
        print("Compresión completada exitosamente.")

    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{input_path}'.")
    except UnidentifiedImageError:
        print(f"Error: No se pudo abrir o reconocer la imagen en '{input_path}'. Asegúrate de que sea un formato de imagen válido y soportado por Pillow.")
    except ValueError as e:
        print(f"Error de valor: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado durante la compresión: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()