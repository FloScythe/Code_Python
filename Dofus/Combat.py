import pyautogui
import time
import random

def Combat():
    if pyautogui.locateOnScreen("Combat/Pret.png", confidence=0.9):
        while True:
        z = pyautogui.locateOnScreen("Combat/invoc1.png", confidence=0.9)
        pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
        pyautogui.click()

        time.sleep(random.uniform(0.1, 0.2))

        z1 = pyautogui.locateOnScreen("Combat/Pos1.png", grayscale=False, confidence=0.6)
        pyautogui.moveTo(z1)
        z2 = pyautogui.locateOnScreen("Combat/Pos2.png", grayscale=False, confidence=0.6)
        pyautogui.moveTo(z2)
        z3 = pyautogui.locateOnScreen("Combat/Pos3.png", grayscale=False, confidence=0.6)
        pyautogui.moveTo(z3)
        z4 = pyautogui.locateOnScreen("Combat/Pos4.png", grayscale=False, confidence=0.6)
        pyautogui.moveTo(z4)

        time.sleep(random.uniform(0.1, 0.2))

        z5 = pyautogui.locateOnScreen("Combat/invoc2.png")
        pyautogui.moveTo(z5,duration=random.uniform(0.1, 0.2))
        pyautogui.click()
        pyautogui.click()

        z6 = pyautogui.locateOnScreen("Combat/Findetour.png", confidence=0.8)
        pyautogui.moveTo(z6, duration=random.uniform(0.1, 0.2))
        pyautogui.click()
        time.sleep(1)

        if pyautogui.locateOnScreen("Combat/Pret.png", confidence=0.9):
