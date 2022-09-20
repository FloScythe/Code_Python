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


# ----Cuivre----
# Map 1
cuivre_x_1 = [525, 448, 525, 784, 863, 1143, 1268, 1348, 1534, 1601]
cuivre_y_1 = [970, 562, 516, 392, 362, 321, 370, 412, 445, 413]
cuivre_ressource_1 = len(cuivre_x_1)

# Map 2
cuivre_x_2 = [876, 946]
cuivre_y_2 = [323, 346]
cuivre_ressource_2 = len(cuivre_x_2)

# Map 3
cuivre_x_3 = [1883, 1741, 1632, 1276, 1123, 1062, 666, 595, 253, 194]
cuivre_y_3 = [945, 588, 595, 389, 413, 437, 482, 446, 579, 604]
cuivre_ressource_3 = len(cuivre_x_3)

cuivre_sortie_0 = [619, 561]
cuivre_sortie_1 = [562, 530]
cuivre_retour_1 = [1984, 1245]
cuivre_retour_0 = [1578, 1238]

while not keyboard.is_pressed('q'):
    time.sleep(random.uniform(0.2, 0.3))
    # Map 1
    for i in range(cuivre_ressource_1):
        recolte(cuivre_x_1[i], cuivre_y_1[i])
    # Map 1 - Sortie
    mouvement(cuivre_sortie_0[0], cuivre_sortie_0[1])
    time.sleep(6)

    # Map 2
    for i in range(cuivre_ressource_2):
        recolte(cuivre_x_2[i], cuivre_y_2[i])
    # Map 2 - Sortie
    mouvement(cuivre_sortie_1[0], cuivre_sortie_1[1])
    time.sleep(6)

    # Map 3
    for i in range(cuivre_ressource_3):
        recolte(cuivre_x_3[i], cuivre_y_3[i])
    # Map 3 - Sortie
    mouvement(cuivre_retour_1[0], cuivre_retour_1[1])
    time.sleep(6)

    # Map 2
    for i in range(cuivre_ressource_2):
        recolte(cuivre_x_2[i], cuivre_y_2[i])
    # Map 2 - Sortie
    mouvement(cuivre_retour_0[0], cuivre_retour_0[1])
    time.sleep(6)

    souris("Ressource/Inventaire.png")
    if pyautogui.locateOnScreen("Ressource/Alerte_full.png", confidence=0.8):
        souris("Ressource/Inventaire.png")
        sell("Ressource/Cuivre.png")
    else:
        souris("Ressource/Inventaire.png")
