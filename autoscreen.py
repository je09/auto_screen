#!/bin/python
from PIL import ImageChops
import pyscreenshot as ImageGrab
from time import sleep
from datetime import datetime

TIMEOUT = 30 # Seconds

image = ImageGrab.grab().convert('RGB') # Get current screen
while True:
    new_image = ImageGrab.grab().convert('RGB') # Get new screen
    sleep(TIMEOUT)
    diff = ImageChops.difference(new_image, image)
    if diff.getbbox():
        new_image.save(f"screen_{datetime.now()}.png")
        image = new_image
        print("screen captured!")
