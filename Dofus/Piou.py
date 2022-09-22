import random
import time

import keyboard
import pyautogui
from Code_Python.Dofus.Function import combat


def Piou():
    while True:
        a = pyautogui.locateOnScreen("../Combat/Piou.png", grayscale=True, confidence=0.8)
        b = pyautogui.locateOnScreen("../Combat/Piou1.png", grayscale=True, confidence=0.8)
        c = pyautogui.locateOnScreen("../Combat/Piou2.png", grayscale=True, confidence=0.8)
        d = pyautogui.locateOnScreen("../Combat/Piou3.png", grayscale=True, confidence=0.8)

        if a or b or c or d:
            z = a
            pyautogui.moveTo(z, duration=random.uniform(0.1, 0.2))
            z = b
            pyautogui.moveTo(z, duration=random.uniform(0.1, 0.2))
            z = c
            pyautogui.moveTo(z, duration=random.uniform(0.1, 0.2))
            z = d
            pyautogui.moveTo(z, duration=random.uniform(0.1, 0.2))
            pyautogui.click()
            time.sleep(0.5)
            if pyautogui.locateOnScreen("../Combat/Attaquer.png", confidence=0.8):
                print("Attaque")
                attack = pyautogui.locateOnScreen("../Combat/Attaquer.png", confidence=0.8)
                pyautogui.moveTo(attack, duration=random.uniform(0.1, 0.3))
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(5)
                break
            elif pyautogui.locateOnScreen("../Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "../Combat/Findetour.png", grayscale=True, confidence=0.8):
                break
    combat(2108, 415)


while not keyboard.is_pressed("q"):
    Piou()
    if pyautogui.locateOnScreen("../Ressource/Repos.png"):
        assis = pyautogui.locateOnScreen("../Combat/assis.png", confidence=0.8)
        pyautogui.moveTo(assis, duration=random.uniform(0.1, 0.3))
        pyautogui.click(clicks=2)
        time.sleep(30)
