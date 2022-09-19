import keyboard
import pyautogui
import time
import random

def combat():
    if pyautogui.locateOnScreen("Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "Combat/Findetour.png", grayscale=True, confidence=0.8):

        p = pyautogui.locateOnScreen("Combat/Pret.png", confidence=0.8)
        pyautogui.moveTo(p, duration=random.uniform(0.1, 0.3))
        pyautogui.click()

        while True:
            z = pyautogui.locateOnScreen("Combat/invoc1.png", confidence=0.8)
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

            z5 = pyautogui.locateOnScreen("Combat/invoc2.png", confidence=0.8)
            pyautogui.moveTo(z5, duration=random.uniform(0.1, 0.3))
            pyautogui.click()
            pyautogui.click()
            time.sleep(0.5)

            if pyautogui.pixelMatchesColor(1794,429,(36,48,18)):
                z6 = pyautogui.locateOnScreen("Combat/Findetour.png", confidence=0.8)
                pyautogui.moveTo(z6, duration=random.uniform(0.1, 0.3))
                pyautogui.click()
                time.sleep(1)

            if pyautogui.locateOnScreen("Combat/Quit.png", confidence=0.8):
                z7 = pyautogui.locateOnScreen("Combat/Quit.png", confidence=0.8)
                pyautogui.moveTo(z7, duration=random.uniform(0.1, 0.3))
                pyautogui.click()
                break
            elif keyboard.is_pressed("q"):
                break
