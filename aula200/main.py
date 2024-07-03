# video aula 337
# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python

from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'original.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new.jpg'

# abrindo a imagem original
pil_image = Image.open(ORIGINAL)

# armazenando o tamanho da imagem
width, height = pil_image.size

# obtendo as informações da imagem - não funcionou (pesquisar)
# exif = pil_image.info['exif']

# redimensionando a imagem
new_width = 640
new_height = round(height * new_width / width)
new_image = pil_image.resize(size=(new_width, new_height))

new_image.save(
    NEW_IMAGE, 
    optimize=True,
    quality=70,
)




