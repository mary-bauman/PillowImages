from PIL import Image, ImageDraw, ImageFont
from os.path import join

# create a new image 
image = Image.new('RGB', (1280,720), (240,240,240))

# create a font 
font = ImageFont.truetype(
	font = join('resources', 'RabbidHighway.otf'), 
	size = 25)

# drawable object
draw = ImageDraw.Draw(image)

# draw text 
draw.text(
	xy = (0,0), 
	text = 'Test', 
	fill = (0,0,0), 
	font = font,
	stroke_width = 2,
	stroke_fill = (255,0,0),
	anchor = 'mm')

image.show()