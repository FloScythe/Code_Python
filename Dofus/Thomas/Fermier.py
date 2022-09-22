import pyautogui
import random
import time
import keyboard


def level_up():
    # Detection en cas de level up
    if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
        up = pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8)
        pyautogui.moveTo(up, duration=random.uniform(0.1, 0.3))
        pyautogui.click()


def souris(nom):
    z = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(0.5)


def combat(x1, y1):
    if pyautogui.locateOnScreen("../Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "../Combat/Findetour.png", grayscale=True, confidence=0.8):

        souris("../Combat/Pret.png")

        while True:
            if pyautogui.pixelMatchesColor(x1, y1 (73, 97, 37)):
                souris("../Combat/invoc_tofu.png")
                souris("../Combat/invoc2.png")
                pyautogui.click()
            else:
                z = pyautogui.locateOnScreen("../Combat/Deplacement.png", confidence=0.8)
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


while not keyboard.is_pressed("q"):
    if pyautogui.locateOnScreen("../Ressource/ble.png",confidence = 0.6):
        z = pyautogui.locateOnScreen("../Ressource/ble.png",confidence = 0.6)
        pyautogui.moveTo(z)
        pyautogui.doubleClick()
    if pyautogui.locateOnScreen("../Ressource/orge.png",confidence = 0.6):
        z = pyautogui.locateOnScreen("../Ressource/orge.png",confidence = 0.6)
        pyautogui.moveTo(z)
        pyautogui.doubleClick()
    level_up()
    #x,y sont les coordonnée du sort tofu au niveau de la couleur vert foncé
    combat(x,y)
