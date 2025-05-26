from PIL import Image, ImageDraw, ImageFont
import os

# create a new image 
image = Image.new('RGB', (1280, 720), (240, 240, 240))

# absolute path to font
script_dir = os.path.dirname(__file__)
font_path = os.path.join(script_dir, 'resources', 'RabbidHighway.otf')

if not os.path.exists(font_path):
    raise FileNotFoundError(f"Font file not found at: {font_path}")

# create font
font = ImageFont.truetype(font_path, size=25)

# drawable object
draw = ImageDraw.Draw(image)

# draw text centered in the image
draw.text(
    xy=(640, 360),  # center of the image
    text='Test',
    fill=(0, 0, 0),
    font=font,
    stroke_width=2,
    stroke_fill=(255, 0, 0),
    anchor='mm'  # middle-middle anchor
)

# show the image
image.show()
