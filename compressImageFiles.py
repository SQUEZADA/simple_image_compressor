from PIL import Image
import os
import json

def compress_image(input_path, output_path, quality):
    """
    Compress an image file using Pillow library.

    Parameters:
        input_path (str): The path to the input image file.
        output_path (str): The path to save the compressed image file.
        quality (int): The quality of the compressed image, from 1 to 95.

    Returns:
        None
    """
    with Image.open(input_path) as img:
        if img.width > img.height:
            img = img.rotate(270, expand=True)
        img.save(output_path, optimize=True, quality=quality)
    print(f"Compressed image saved at {output_path}")

# Example usage
images = open("directus_files 20230329-155710.json", "r")
for x in images:
  fileInfo = json.loads(x)
  fileTypes = ['image/jpeg','image/jpg','image/png']
  imageCount = 0
  for y in fileInfo:
    if fileTypes.count( y["type"] ):
        input_file = f'/{y["filename_download"]}'
        output_file = f'/compress/image{imageCount}.webp'
        compress_image(input_file, output_file, quality=60)
        imageCount+=1
images.close()

