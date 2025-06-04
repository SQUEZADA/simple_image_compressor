# Compresor de Imágenes Simple

Este proyecto implementa un compresor de imágenes modular y extensible, construido con una arquitectura orientada a objetos. Permite cargar, comprimir y convertir imágenes entre diferentes formatos, utilizando varios algoritmos de compresión.

---

## Características Implementadas

* **Arquitectura Orientada a Objetos (POO):** El diseño del compresor se basa en principios POO, lo que facilita la adición de nuevos formatos de imagen y algoritmos de compresión sin modificar el código existente de manera extensiva.
    * **Manejadores de Imagen (Image Handlers):** Clases específicas para cargar y guardar diferentes formatos de imagen.
    * **Algoritmos de Compresión:** Clases que encapsulan la lógica de distintos métodos de compresión.
* **Formatos de Imagen Soportados:**
    * **JPEG/JPG:** Compresión con pérdida, ideal para fotografías.
    * **PNG:** Compresión sin pérdida, ideal para gráficos con transparencia o ilustraciones.
    * **WebP:** Un formato moderno que ofrece una compresión superior (con pérdida y sin pérdida) con soporte para transparencia.
* **Algoritmos de Compresión Disponibles:**
    * **Compresión con Pérdida (`lossy`):** Reduce el tamaño del archivo eliminando información. Adecuado para JPEG y WebP (por defecto).
    * **Compresión sin Pérdida (`lossless`):** Reduce el tamaño del archivo sin perder ninguna información original de la imagen. Ideal para PNG y WebP.
    * **Calidad Adaptativa (`adaptive_quality`):** Una estrategia que, en teoría, ajustaría la calidad de compresión de forma inteligente. Actualmente, se comporta como una compresión con pérdida normal, pero abre la puerta a futuras implementaciones más avanzadas.
    * **Reducción de Paleta (`palette_reduction`):** Reduce el número de colores en una imagen, útil para optimizar PNGs con muchos colores o para conversiones a formatos con paleta limitada.

---

## Cómo Usar

Asegúrate de tener Python instalado (versión 3.x recomendada) y las librerías necesarias (principalmente `Pillow`).

1.  **Instalación de dependencias:**
    ```bash
    pip install Pillow
    ```

2.  **Estructura del Proyecto:**
    Asegúrate de que tu proyecto tenga la siguiente estructura de carpetas y archivos, y que los archivos `__init__.py` estén presentes y vacíos en las carpetas `image_formats/` y `compression_algorithms/`.

    ```
    simple_image_compressor/
    ├── compression_algorithms/
    │   ├── __init__.py
    │   ├── compression_algorithm_base.py
    │   ├── lossless_compression.py
    │   ├── lossy_compression.py
    │   ├── adaptive_quality_compression.py
    │   └── palette_reduction_compression.py
    ├── image_formats/
    │   ├── __init__.py
    │   ├── image_handler_base.py
    │   ├── jpg_handler.py
    │   ├── png_handler.py
    │   └── webp_handler.py
    ├── compressor.py
    └── README.md
    ```

3.  **Ejecución desde la Línea de Comandos (CLI):**

    Navega a la raíz de tu proyecto (`simple_image_compressor/`) en tu terminal y ejecuta `compressor.py` con los siguientes argumentos:

    ```bash
    python compressor.py <input_path> <output_path> [opciones]
    ```

    **Argumentos:**
    * `<input_path>`: Ruta a la imagen original que deseas comprimir.
    * `<output_path>`: Ruta y nombre del archivo donde se guardará la imagen comprimida. La extensión del archivo de salida (`.jpg`, `.png`, `.webp`) determinará el formato de salida.

    **Opciones:**
    * `--quality <valor>`: (Opcional) Nivel de calidad para la compresión con pérdida (0-100). Por defecto es 85. Para WebP sin pérdida, esto afecta el esfuerzo de compresión.
    * `--algorithm <nombre_algoritmo>`: (Opcional) Especifica el algoritmo de compresión. Los valores posibles son: `lossy` (por defecto), `lossless`, `adaptive_quality`, `palette_reduction`.
    * `--colors <número>`: (Opcional) Número máximo de colores para el algoritmo `palette_reduction`. Por defecto es 256.

---

## Ejemplos de Uso

* **Comprimir una imagen JPG a JPG con calidad 60 (usando algoritmo lossy por defecto):**
    ```bash
    python compressor.py mi_foto.jpg mi_foto_comprimida.jpg --quality 60
    ```

* **Convertir PNG a WebP con compresión sin pérdida:**
    ```bash
    python compressor.py grafico.png grafico_optimo.webp --algorithm lossless
    ```

* **Convertir JPG a PNG (sin compresión adicional en PNG, mantiene la calidad visual):**
    ```bash
    python compressor.py foto.jpg foto_png.png
    ```
    *(Nota: PNG es sin pérdida, `--quality` no tendrá efecto directo en PNG, pero se pasará al handler por consistencia.)*

* **Reducir la paleta de colores de un PNG a 128 colores y guardarlo como PNG:**
    ```bash
    python compressor.py icono_multicolor.png icono_reducido.png --algorithm palette_reduction --colors 128
    ```