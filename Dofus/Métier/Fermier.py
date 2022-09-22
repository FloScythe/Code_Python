import pyautogui
import random
import time
import keyboard

while keyboard.is_pressed('q') == False:
    pyautogui.moveTo(pyautogui.locateOnScreen("../Ressource/ble.png"),confidence=0.8)
    pyautogui.click()
