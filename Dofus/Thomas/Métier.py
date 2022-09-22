import pyautogui
import random
import time
import keyboard

while not keyboard.is_pressed("q"):
    if pyautogui.locateOnScreen("../Ressource/ble.png",confidence = 0.6):
        z = pyautogui.locateOnScreen("../Ressource/ble.png",confidence = 0.6)
        pyautogui.moveTo(z)
        pyautogui.doubleClick()
    if pyautogui.locateOnScreen("../Ressource/orge.png",confidence = 0.6):
        z = pyautogui.locateOnScreen("../Ressource/orge.png",confidence = 0.6)
        pyautogui.moveTo(z)
        pyautogui.doubleClick()