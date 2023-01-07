# RPI-Adafruit_ssd1306-monitor-python

![img](https://lh3.googleusercontent.com/pw/AL9nZEUw0f0gHWmv4VvhXlT07a-jbTBSpCk2ywxk3NxR4OfT2gPtdiaCEcqRHorEoF5BLmc2YtJGFi-2NQZiA9ghP_ic7uEy4Pai2uGE68cUk53CuPJYsQz2-NkMQgHvAI5jOGcPCSz-sVe1A1SaFpbPx5v2=w2880-h948-no?authuser=0)



## Install pip and ssd1306 library 

- install pip3
 ```console
sudo apt-get install python3-pip
```
- install Python Imaging Library
```console
pip3 install --upgrade Pillow
```
- install  SSD1306 Library
```console
pip3 install adafruit-circuitpython-ssd1306
```
## Install psutil
- install psutil
```console
pip3 install psutil
```

## Test
```console
python3 OledMon.py
```
-make Oledmon.py executable and test
```console
chmod +x OledMon.py 
```
```console
./OledMon.py
```

## Run OledMon as service
move OledMon.service to /lib/systemd/system/
```console
sudo mv OledMon.service /lib/systemd/system/
```
-enable service
```console
sudo systemctl enable OledMon.service
```
- reboot


full [SSD1306 documentation](https://learn.adafruit.com/monochrome-oled-breakouts/python-usage-2)



