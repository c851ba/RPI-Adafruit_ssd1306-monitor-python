import board
import busio
import adafruit_ssd1306
import digitalio
import socket
from PIL import Image, ImageDraw, ImageFont

from gpiozero import CPUTemperature
import psutil
from psutil._common import bytes2human
import time
import datetime 


import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 1))  # connect() for UDP doesn't send packets
local_ip_address = s.getsockname()[0]
print(local_ip_address)

print(os.name)



print(os.popen('uptime -p').read()[0:10])




