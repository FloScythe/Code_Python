import pyautogui
import random
import time
import keyboard


def souris(nom):
    z = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(1)


def sell():
    souris("Ressource/Inventaire.png")
    souris("Ressource/Ressource_Inventaire.png")
    souris("Ressource/fer.png")
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
                break
            elif keyboard.is_pressed("q"):
                break


def level_up():
    # Detection en cas de level up
    if pyautogui.locateOnScreen("Combat/Quit.png", confidence=0.8):
        up = pyautogui.locateOnScreen("Combat/Quit.png", confidence=0.8)
        pyautogui.moveTo(up, duration=random.uniform(0.1, 0.3))
        pyautogui.click()


def recolte(x, y):
    time.sleep(0.5)
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(0.5)
    if pyautogui.locateOnScreen("Ressource/Fenetre_vide.png", confidence=0.7):
        time.sleep(2)
        pass
    else:
        time.sleep(12)
    level_up()
    combat()


# Map 1
liste_x_1 = [936, 1205, 1267, 1810, 1876]
liste_y_1 = [804, 414, 429, 691, 716]
ressource_1 = len(liste_x_1)
repos1 = 4 * random.uniform(12, 12.5)

# Map 2
liste_x_2 = [1755, 1681, 1606, 1286, 1039, 996, 811, 729, 386, 315]
liste_y_2 = [798, 763, 734, 581, 558, 524, 602, 644, 818, 858]
ressource_2 = len(liste_x_2)
repos2 = 4 * random.uniform(12, 12.5)

# Map 3
liste_x_3 = [1551, 1481, 1408, 1274, 1192, 395, 327]
liste_y_3 = [644, 609, 576, 542, 582, 708, 750]
ressource_3 = len(liste_x_3)
repos3 = 4 * random.uniform(12, 12.5)

# Trajet
go_out_0 = [979, 677]
go_out_1 = [493, 905]
go_out_2 = [686, 730]  # Map vide

go_back_2 = [1635, 999]
go_back_1 = [1499, 1132]  # Map vide
go_back_0 = [1511, 1073]

while not keyboard.is_pressed('q'):
    pyautogui.moveTo(2264,1268, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(random.uniform(0.2, 0.3))
    # Map 1
    for i in range(ressource_1):
        recolte(liste_x_1[i], liste_y_1[i])

    pyautogui.moveTo(go_out_0[0], go_out_0[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(6)

    if keyboard.is_pressed('q'):
        print("Interruption de la boucle")
        break

    # Map 2
    for i in range(ressource_2):
        recolte(liste_x_2[i], liste_y_2[i])

    pyautogui.moveTo(go_out_1[0], go_out_1[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(6)

    # Entree map vide
    pyautogui.moveTo(go_out_2[0], go_out_2[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(6)
    # Sorti map vide

    if keyboard.is_pressed('q'):
        print("Interruption de la boucle")
        break

    # Map 3
    for i in range(ressource_3):
        recolte(liste_x_3[i], liste_y_3[i])

    pyautogui.moveTo(go_back_2[0], go_back_2[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(6)

    pyautogui.moveTo(go_back_1[0], go_back_1[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(6)

    # Map 2
    for i in range(ressource_2):
        recolte(liste_x_2[i], liste_y_2[i])

    pyautogui.moveTo(go_back_0[0], go_back_0[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(5)

    souris("Ressource/Inventaire.png")
    if pyautogui.locateOnScreen("Ressource/Alerte_full.png", confidence=0.8):
        souris("Ressource/Inventaire.png")
        sell()
    else:
        souris("Ressource/Inventaire.png")
