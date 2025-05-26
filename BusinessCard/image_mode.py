from PIL import Image
import os

script_dir = os.path.dirname(__file__)
image1_path = os.path.join(script_dir, 'resources', 'cat_bw.jpg')
image2_path = os.path.join(script_dir, 'resources', 'raccoon.png')

image1 = Image.open(image1_path).convert('RGB')
image2 = Image.open(image2_path).convert('1')

image1.paste(image2, (100, 400))

image1.show()
