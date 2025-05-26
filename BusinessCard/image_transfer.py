from PIL import Image, ImageChops 
import os

script_dir = os.path.dirname(__file__)
cat = Image.open(os.path.join(script_dir, 'resources', 'cat.jpg'))
dog = Image.open(os.path.join(script_dir, 'resources', 'dog.jpg'))
raccoon = Image.open(os.path.join(script_dir, 'resources', 'raccoon.png'))
checkerboard = Image.open(os.path.join(script_dir, 'resources', 'checkerboard.png'))
circle = Image.open(os.path.join(script_dir, 'resources', 'circle.png'))
bird = Image.open(os.path.join(script_dir, 'resources', 'card', 'bird.png'))


# paste an image with a mask
cat.paste(
	im = bird, 
	box = (100,200), 
	mask = bird)

# paste an image with a blending mode 
image_chops = ImageChops.overlay(dog, cat)


image_chops.show()