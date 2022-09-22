import random
import time
import keyboard
import pyautogui


def souris(nom):
    z = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(1)


def mouvement(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()


def combat(x, y):
    if pyautogui.locateOnScreen("../Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "../Combat/Findetour.png", grayscale=True, confidence=0.8):

        souris("../Combat/Pret.png")

        while True:
            souris("../Combat/invoc1.png")
            time.sleep(random.uniform(0.1, 0.2))
            # z1 = pyautogui.locateOnScreen("../Combat/Pos1.png", grayscale=False, confidence=0.6)
            # z2 = pyautogui.locateOnScreen("../Combat/Pos2.png", grayscale=False, confidence=0.6)
            # z3 = pyautogui.locateOnScreen("../Combat/Pos3.png", grayscale=False, confidence=0.6)
            # z4 = pyautogui.locateOnScreen("../Combat/Pos4.png", grayscale=False, confidence=0.6)
            if not pyautogui.pixelMatchesColor(x, y, (36, 48, 18)):
                souris("../Combat/invoc2.png")
                pyautogui.click()
            else:
                z = pyautogui.locateOnScreen("../Combat/Deplacement.png", confidence=0.8)
                pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
                pyautogui.click(clicks=2)
                time.sleep(0.5)
                souris("../Combat/Findetour.png")
                time.sleep(1)

            if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
                souris("../Combat/Quit.png")
                time.sleep(1)
                if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
                    level_up()
                break
            elif keyboard.is_pressed("q"):
                time.sleep(1)
                break


def level_up():
    # Detection en cas de level up
    if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
        up = pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8)
        pyautogui.moveTo(up, duration=random.uniform(0.1, 0.3))
        pyautogui.click()


def recolte(x, y, a, b):
    combat(a, b)
    level_up()
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.2))
    pyautogui.click(duration=0.2)
    time.sleep(0.5)
    if pyautogui.locateOnScreen("../Ressource/Fenetre_vide.png", confidence=0.6):
        pass
    else:
        time.sleep(13)


def sell(x):
    souris("../Ressource/Inventaire.png")
    souris("../Ressource/Ressource_Inventaire.png")
    souris(x)
    souris("../Ressource/hdv.png")
    souris("../Ressource/QTE100.png")
    if pyautogui.locateOnScreen("../Ressource/Entrer.png"):
        souris("../Ressource/Entrer.png")
        souris("../Ressource/Mettre_en_vente.png")
        souris("../Ressource/Vente.png")
        souris("../Combat/Quit.png")
    else:
        souris("../Combat/Quit.png")
