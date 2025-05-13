from PIL import Image, ImageDraw, ImageFont
from os.path import join

# create a new image 
image = Image.new('RGB', (1280,720), (30,30,30))

# create a font 
font = ImageFont.truetype(
	font = join('resources', 'RabbidHighway.otf'), 
	size = 25)

# drawable object
draw = ImageDraw.Draw(image)

# multiline text 
draw.multiline_text(
	xy = (100,200),
	text = 'First line\nSecond line',
	font = font,
	spacing = 200)

# get text size 
draw.rectangle(xy = font.getbbox('First line'))
draw.rectangle(
	xy = draw.multiline_textbbox(
		xy = (100,200),
		text = 'First line\nSecond line',
		font = font,
		spacing = 200))

# show the image
image.show()