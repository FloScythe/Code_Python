import keyboard
import pyautogui
import time
import random


def souris(nom):
    z = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(0.5)


def level_up():
    # Detection en cas de level up
    if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
        up = pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8)
        pyautogui.moveTo(up, duration=random.uniform(0.1, 0.3))
        pyautogui.click()


def combat(x3, y3, x4, y4):
    if pyautogui.locateOnScreen("../Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "../Combat/Findetour.png", grayscale=True, confidence=0.8):

        souris("../Combat/Pret.png")

        while True:
            # if pyautogui.pixelMatchesColor(x1, y1, (73, 97, 37)):
            #     souris("../Combat/invoc_sanglier.png")
            #     souris("../Combat/invoc2.png")
            #     pyautogui.click()
            # elif pyautogui.pixelMatchesColor(x2, y2, (46, 93, 107)):
            #     souris("../Combat/invoc_bouf.png")
            #     souris("../Combat/invoc2.png")
            #     pyautogui.click()
            if pyautogui.pixelMatchesColor(x3, y3, (73, 97, 37)):
                souris("../Combat/invoc_tofu.png")
                souris("../Combat/invoc2.png")
                pyautogui.click()
            elif pyautogui.pixelMatchesColor(x4, y4, (94, 154, 171)):
                souris("../Combat/Sort_1.png")
                pyautogui.moveTo(pyautogui.locateOnScreen("../Combat/Perso.png"), confidence=0.8)
                pyautogui.moveRel(200, None)
                pyautogui.click()
            else:
                z = pyautogui.locateOnScreen("../Combat/Deplacement.png", confidence=0.8)
                pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
                pyautogui.doubleClick()
                time.sleep(0.5)
                souris("../Combat/Findetour.png")
                time.sleep(1)

            if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
                if pyautogui.locateOnScreen("../Combat/dead.png", confidence=0.8):
                    pyautogui.moveTo(2753, 769)
                    pyautogui.click()
                    keyboard.send("ctrl+F2")
                    time.sleep(1)
                souris("../Combat/Quit.png")
                time.sleep(1)
                if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
                    level_up()
                # souris("../Ressource/Inventaire.png")
                # souris("../Ressource/sac.png")
                # pyautogui.click()
                break
            elif keyboard.is_pressed("q"):
                time.sleep(1)
                break


combat(2109, 418, 2109, 318)
