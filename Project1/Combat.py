import pyautogui
import keyboard
import time
import random

while keyboard.is_pressed('q') == False:
    z = pyautogui.locateOnScreen("invoc1.png", grayscale=False, confidence=0.8)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()

    time.sleep(random.uniform(0.1, 0.2))

    z1 = pyautogui.locateOnScreen("Pos1.png", grayscale=False, confidence=0.5)
    pyautogui.moveTo(z1)
    z2 = pyautogui.locateOnScreen("Pos2.png", grayscale=False, confidence=0.5)
    pyautogui.moveTo(z2)
    z3 = pyautogui.locateOnScreen("Pos3.png", grayscale=False, confidence=0.5)
    pyautogui.moveTo(z3)
    z4 = pyautogui.locateOnScreen("Pos4.png", grayscale=False, confidence=0.5)
    pyautogui.moveTo(z4)

    time.sleep(random.uniform(0.1, 0.2))

    z5 = pyautogui.locateOnScreen("invoc2.png")
    pyautogui.moveTo(z5,duration=random.uniform(0.1, 0.2))
    pyautogui.click()
    pyautogui.click()

    z6 = pyautogui.locateOnScreen("Findetour.png", confidence=0.8)
    pyautogui.moveTo(z6, duration=random.uniform(0.1, 0.2))
    pyautogui.click()