#!/bin/python
from PIL import ImageChops # $ pip install pillow
import pyscreenshot as ImageGrab # $ pip install pyscreenshot
from time import sleep
from datetime import datetime

image = ImageGrab.grab().convert('RGB')
while True:
    new_image = ImageGrab.grab().convert('RGB')
    sleep(2)
    diff = ImageChops.difference(new_image, image)
    if diff.getbbox():
        new_image.save(f"screen_{datetime.now()}.png")
        image = new_image
        print("screen captured!")
