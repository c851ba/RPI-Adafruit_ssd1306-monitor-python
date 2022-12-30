#!/usr/bin/env python3

import board
import busio
import adafruit_ssd1306
import digitalio
import psutil
import time
import socket
from datetime import datetime
from gpiozero import CPUTemperature
from psutil._common import bytes2human
from PIL import Image, ImageDraw, ImageFont

#screen transition and srefresh
Transition = 5
Refresh = 1

######################### init display ##############################################
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
######################################################################################

#################### Create blank image for drawing ##################################
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Set font
fontsize = 15
#font = ImageFont.load_default()
# use a truetype font
font = ImageFont.truetype("arial.ttf", fontsize)
fontb = ImageFont.truetype("arialbold.ttf", fontsize)
#######################################################################################

#########################################################################################################
## align text 
# text = "Hello World!" 
# (font_width, font_height) = font.getsize(text)
# draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2), text, font=font, fill=255)
#########################################################################################################
while True:    
    # time
    for _ in range(Transition):
        draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
        text= 'Time'
        current_time = datetime.now().strftime("%H:%M:%S")
        (font_width, font_height) = font.getsize(text)
        draw.text((oled.width//2 - font_width//2, 0), text, font=fontb, fill=255)

        (font_width, font_height) = font.getsize(current_time)
        draw.text((oled.width//2 - font_width//2, oled.height//2 - font_height//2), current_time, font=font, fill=255)
        oled.image(image)
        oled.show()
        time.sleep(Refresh)

    # cpu used
    for _ in range(Transition):
        cpu = str(psutil.cpu_percent()) + '%'
        temp = str(int(CPUTemperature().temperature))+ '°C'
        LA= str(psutil.getloadavg()[0])
        draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
        CPUusage= ('CPU: '+ cpu)
        CPUTemp =('CPU Temp: '+ temp) 
        (font_width, font_height) = font.getsize('CPU')
        draw.text((oled.width//2 - font_width//2,0), 'CPU', font=fontb, fill=255)
        draw.text((0,fontsize), 'Usage: '+ cpu, font=font, fill=255)
        draw.text((0,fontsize*2), 'Temp:  '+ temp, font=font, fill=255)
        draw.text((0,fontsize*3), 'Load: '+ LA, font=font, fill=255)
        oled.image(image)
        oled.show()
        time.sleep(Refresh)
    

    # RAM
    for _ in range(Transition):
        ramUsed = (bytes2human(psutil.virtual_memory()[3]))
        ramFree = (bytes2human(psutil.virtual_memory()[4]))
        rampct =  str(psutil.virtual_memory()[2])
        draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
        # CPUusage= ('CPU: '+ cpu)
        # CPUTemp =('CPU Temp: '+ temp) 
        (font_width, font_height) = font.getsize('RAM')
        draw.text((oled.width//2 - font_width//2,0), 'RAM', font=fontb, fill=255)
        draw.text((0,fontsize), 'Used: '+ ramUsed, font=font, fill=255)
        draw.text((0,fontsize*2), 'Free: '+ ramFree, font=font, fill=255)
        draw.text((0,fontsize*3), 'Used: '+ rampct+'%', font=font, fill=255)

        oled.image(image)
        oled.show()
        time.sleep(Refresh)

    # System
    for _ in range(Transition):
        draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
        IPAddress = s.getsockname()[0]
        
        (font_width, font_height) = font.getsize('System info')
        draw.text((oled.width//2 - font_width//2,0), 'System info', font=fontb, fill=255)
        #draw.text((0,fontsize), 'L1', font=font, fill=255)
        draw.text((0,fontsize*2), 'IP: '+ IPAddress, font=font, fill=255)
        #draw.text((0,fontsize*3), 'l3: ', font=font, fill=255)

        oled.image(image)
        oled.show()
        time.sleep(Refresh)
        