#!/usr/bin/env python3

import board
import busio
import adafruit_ssd1306
import digitalio
from PIL import Image, ImageDraw, ImageFont

# # Define the Reset Pin
reset_pin = digitalio.DigitalInOut(board.D4) 

# # Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# # Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=reset_pin)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Load default font.
#font = ImageFont.load_default()
# use a truetype font
font = ImageFont.truetype("arial.ttf", 18)

text = "Hello World!" 
(font_width, font_height) = font.getsize(text)
draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2), text, font=font, fill=255)
# draw.text((0, 16), "Line2", font=font, fill=255)
# draw.text((0, 32), "Line3", font=font, fill=255)
#draw.text((0, 48), "Line4", font=font, fill=255)        

# Display image
oled.image(image)
oled.show()
