from PIL import Image, ImageDraw, ImageFont
import os

# create a new image 
image = Image.new('RGB', (1280, 720), (30, 30, 30))

# absolute path to font
script_dir = os.path.dirname(__file__)
font_path = os.path.join(script_dir, 'resources', 'RabbidHighway.otf')

if not os.path.exists(font_path):
    raise FileNotFoundError(f"Font file not found at: {font_path}")

# create font
font = ImageFont.truetype(font_path, size=25)

# drawable object
draw = ImageDraw.Draw(image)

# multiline text 
draw.multiline_text(
    xy=(100, 200),
    text='First line\nSecond line',
    font=font,
    spacing=200)

# draw bounding box around first line text
bbox = font.getbbox('First line')
draw.rectangle(bbox, outline='red')

# show the image
image.show()
