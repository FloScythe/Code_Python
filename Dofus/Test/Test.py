import random
import time

import keyboard
import pyautogui

from Code_Python.Dofus.Function import souris, level_up


def combat(x1, y1, x2, y2, x3, y3):
    if pyautogui.locateOnScreen("../Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "../Combat/Findetour.png", grayscale=True, confidence=0.8):

        souris("../Combat/Pret.png")

        while True:
            if pyautogui.pixelMatchesColor(x1, y1, (73, 97, 37)):
                souris("../Combat/invoc_sanglier.png")
                souris("../Combat/invoc2-2.png")
                pyautogui.click()
            elif pyautogui.pixelMatchesColor(x2, y2, (46, 93, 107)):
                souris("../Combat/invoc_bouf.png")
                souris("../Combat/invoc2-2.png")
                pyautogui.click()
            elif pyautogui.pixelMatchesColor(x3, y3, (73, 97, 37)):
                souris("../Combat/invoc_tofu.png")
                souris("../Combat/invoc2-2.png")
                pyautogui.click()
            else:
                z = pyautogui.locateOnScreen("../Combat/Deplacement-2.png", confidence=0.8)
                pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
                pyautogui.doubleClick()
                time.sleep(0.5)
                souris("../Combat/Findetour.png")
                time.sleep(1)

            if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
                souris("../Combat/Quit.png")
                time.sleep(1)
                if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
                    level_up()
                souris("../Ressource/Inventaire.png")
                souris("../Ressource/sac.png")
                pyautogui.click()
                break
            elif keyboard.is_pressed("q"):
                time.sleep(1)
                break


combat(2109, 421, 2099, 329,2107,890)
