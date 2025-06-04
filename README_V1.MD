# Simple Image Compressor

Este es un compresor de imágenes simple escrito en Python que permite comprimir imágenes en formatos PNG y JPG utilizando diferentes algoritmos de compresión.

## Uso

Ejecuta el script `compressor.py` desde la línea de comandos con los siguientes argumentos:

```bash
python compressor.py <ruta_entrada> <ruta_salida> [--quality <0-100>] [--algorithm <lossy|lossless>]
```

Argumentos:
1. **<ruta_entrada>**: La ruta al archivo de imagen que deseas comprimir.
2. **<ruta_salida>**: La ruta donde se guardará la imagen comprimida. La extensión del archivo de salida determinará el formato (por ejemplo, .jpg para JPEG, .png para PNG).
3. **--quality <0-100> (opcional)**: Nivel de calidad para la compresión con pérdida (por ejemplo, para JPG). El valor predeterminado es 85.
4. **--algorithm <lossy|lossless> (opcional)**: El algoritmo de compresión a utilizar. Las opciones disponibles son lossy (con pérdida, predeterminado) y lossless (sin pérdida).

Ejemplos:
```bash
python compressor.py image.png compressed.png --algorithm lossless

python compressor.py photo.jpg smaller.jpg --quality 60

python compressor.py banner.png banner.jpg --algorithm lossy --quality 75
```

### **Formatos Soportados**

Los formatos de imagen soportados se gestionan de forma modular en la carpeta ``image_formats``. Actualmente, se incluyen los siguientes formatos:

- PNG
- JPEG (.jpg, .jpeg)

### Algoritmos de Compresión

- lossy: Compresión con pérdida (adecuada para JPG).
- lossless: Compresión sin pérdida (adecuada para PNG).


### Estructura del Proyecto
```bash
    simple_image_compressor/
    ├── compression_algorithms/
    │   ├── lossless_compression.py
    │   └── lossy_compression.py
    ├── image_formats/
    │   ├── jpg_handler.py
    │   └── png_handler.py
    └── compressor.py
```

## **Requisitos**
- Python 3
- Pillow (pip install Pillow)

## **Próximos Pasos**
- Agregar soporte para más formatos de imagen (e.g., GIF, WebP).
- Implementar algoritmos de compresión adicionales con más opciones de configuración.
- Mejorar la documentación con ejemplos más detallados y explicaciones técnicas.
- Considerar la posibilidad de añadir una interfaz gráfica de usuario (GUI) utilizando librerías como Tkinter o PyQt.
- Implementar pruebas unitarias para asegurar la calidad y el correcto funcionamiento del código.
- Explorar opciones para optimizar aún más la compresión y el rendimiento.