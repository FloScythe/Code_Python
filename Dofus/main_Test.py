import pyautogui
import random
import time
import keyboard


def souris(nom):
    z = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(1)


def mouvement(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()


def sell(x):
    souris("Ressource/Inventaire.png")
    souris("Ressource/Ressource_Inventaire.png")
    souris(x)
    souris("Ressource/hdv.png")
    souris("Ressource/QTE100.png")
    souris("Ressource/Entrer.png")
    souris("Ressource/Mettre_en_vente.png")
    souris("Ressource/Vente.png")
    souris("Combat/Quit.png")


def combat():
    if pyautogui.locateOnScreen("Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "Combat/Findetour.png", grayscale=True, confidence=0.8):

        souris("Combat/Pret.png")

        while True:
            souris("Combat/invoc1.png")

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

            souris("Combat/invoc2.png")
            pyautogui.click()
            time.sleep(0.5)

            if pyautogui.pixelMatchesColor(1794, 429, (36, 48, 18)):
                souris("Combat/Findetour.png")
                time.sleep(1)

            if pyautogui.locateOnScreen("Combat/Quit.png", confidence=0.8):
                souris("Combat/Quit.png")
                time.sleep(1)
                break
            elif keyboard.is_pressed("q"):
                time.sleep(1)
                break


def level_up():
    # Detection en cas de level up
    if pyautogui.locateOnScreen("Combat/Quit.png", confidence=0.8):
        up = pyautogui.locateOnScreen("Combat/Quit.png", confidence=0.8)
        pyautogui.moveTo(up, duration=random.uniform(0.1, 0.3))
        pyautogui.click()


def recolte(x, y):
    level_up()
    combat()
    pyautogui.moveTo(x, y, duration=random.uniform(1, 1.3))
    pyautogui.click()
    if pyautogui.locateOnScreen("Ressource/Fenetre_vide.png", confidence=0.6):
        time.sleep(0.5)
        pass
    else:
        time.sleep(12)


# Map
Test_x_1 = []
Test_y_1 = []
Test_ressource_1 = len(Test_x_1)
Test_go_out_0 = [979, 677]
Test_go_back_0 = [1511, 1073]

minerai = input("Quel minerai à prendre ?")
mouvement(2264, 1268)


while not keyboard.is_pressed('q'):
    time.sleep(random.uniform(0.2, 0.3))
    # Map 1
    for i in range(Test_ressource_1):
        recolte(Test_x_1[i], Test_y_1[i])
    # Map 1 - Sortie
    mouvement(Test_go_out_0[0], Test_go_out_0[1])
    time.sleep(6)

    souris("Ressource/Inventaire.png")
    if pyautogui.locateOnScreen("Ressource/Alerte_full.png", confidence=0.8):
        souris("Ressource/Inventaire.png")
        sell("Ressource/Fer.png")
    else:
        souris("Ressource/Inventaire.png")