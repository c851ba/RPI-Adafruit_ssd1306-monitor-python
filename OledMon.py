#!/usr/bin/env python3

import board
import busio
import adafruit_ssd1306
import digitalio
from PIL import Image, ImageDraw, ImageFont

from gpiozero import CPUTemperature
import psutil
from psutil._common import bytes2human
import time
from datetime import datetime

#Refresh
Refresh = 1.0
######################### init display #####################################
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
##############################################################################

# Create blank image for drawing.

# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Set font
fontsize = 16
#font = ImageFont.load_default()
# use a truetype font
font = ImageFont.truetype("arial.ttf", fontsize)

# text = "Hello World!" 
# (font_width, font_height) = font.getsize(text)
# draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2), text, font=font, fill=255)
# #draw.text((0, 0), "Line2", font=font, fill=255)
# #draw.text((0, font_height), "Line3", font=font, fill=255)
# #draw.text((0, font_height*2), "Line4", font=font, fill=255)        
# # Display image
# oled.image(image)
# oled.show()


# image.write_bmp_img(name="raspberry.bmp",offX=64,offY=16,invert=True)
# oled.image(image)
# oled.show()


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    cpu = str(psutil.cpu_percent()) + '%'
    temp = str(int(CPUTemperature().temperature))+ '°C'
    ramUsed = (psutil.virtual_memory()[3])
    ramFree = (psutil.virtual_memory()[4])

    #ramUsed = 'RAM Used ' + str(bytes2human(ramUsed))
    #ramFree = 'RAM Free ' + str(bytes2human(ramFree))
    ramUsed = (bytes2human(ramUsed))
    ramFree = (bytes2human(ramFree))
    #rampct = 'RAM Used (GB):' + str(psutil.virtual_memory()[3]/1000000000)
    
    # time
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    Time= ('Time: ' + current_time)
    (font_width, font_height) = font.getsize(Time)
    draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2), Time, font=font, fill=255)
    oled.image(image)
    oled.show()
    time.sleep(Refresh)
    
    # cpu used
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
    CPUusage= ('CPU: '+ cpu)
    CPUTemp =('CPU Temp: '+ temp) 
    (font_width, font_height) = font.getsize('CPU')
    draw.text((oled.width//2 - font_width//2,0), 'CPU', font=font, fill=255)
    draw.text((0,fontsize), 'Usage: '+ cpu, font=font, fill=255)
    draw.text((0,fontsize*2), 'Temp: '+ temp, font=font, fill=255)
    oled.image(image)
    oled.show()
    time.sleep(Refresh)
    


    # # cpu temp
    # lcd.clear()
    # lcd.cursor_pos = (0, 0)
    # lcd.write_string('CPU Temperature: ')
    # lcd.cursor_pos = (1, 0)
    # lcd.write_string(temp)
    # time.sleep(3)
    # # ram free 
    # lcd.clear()
    # lcd.cursor_pos = (0, 0)
    # lcd.write_string('Memory Free')
    # lcd.cursor_pos = (1, 0)
    # lcd.write_string(ramFree)
    # time.sleep(3)
    # # ram used
    # lcd.clear()
    # lcd.cursor_pos = (0, 0)
    # lcd.write_string('Memory Used') 
    # lcd.cursor_pos = (1, 0)
    # lcd.write_string(ramUsed)
    # time.sleep(Refresh)