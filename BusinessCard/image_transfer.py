from PIL import Image, ImageChops 
from os.path import join 

cat = Image.open(join('resources', 'cat.jpg'))
dog = Image.open(join('resources', 'dog.jpg'))
raccoon = Image.open(join('resources', 'raccoon.png'))
checkerboard = Image.open(join('resources', 'checkerboard.png'))
circle = Image.open(join('resources', 'circle.png'))
bird = Image.open(join('resources', 'card', 'bird.png'))


# paste an image with a mask
# cat.paste(
# 	im = bird, 
# 	box = (100,200), 
# 	mask = bird)

# paste an image with a blending mode 
image_chops = ImageChops.overlay(dog, cat)


image_chops.show()