import cv2
import numpy
import pyautogui
from PIL import ImageGrab
import time


def display_mouse_position():
    while True:
        x, y = pyautogui.position()
        print(f"Position de la souris : ({x}, {y})")
        time.sleep(2)


# display_mouse_position()
pyautogui.moveTo(506, 155)

