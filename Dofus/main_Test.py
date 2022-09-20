import pyautogui
import random
import time
import keyboard


def souris(nom):
    z = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(1)


def mouvement(x,y):
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
                break
            # elif keyboard.is_pressed("q"):
            #     break


def level_up():
    # Detection en cas de level up
    if pyautogui.locateOnScreen("Combat/Quit.png", confidence=0.8):
        up = pyautogui.locateOnScreen("Combat/Quit.png", confidence=0.8)
        pyautogui.moveTo(up, duration=random.uniform(0.1, 0.3))
        pyautogui.click()


def recolte(x, y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(1)
    if pyautogui.locateOnScreen("Ressource/Fenetre_vide.png", confidence=0.6):
        time.sleep(0.5)
        pass
    else:
        time.sleep(12)
    level_up()
    combat()

#----Fer----
# Map 1
fer_x_1 = [936, 1205, 1267, 1810, 1876]
fer_y_1 = [804, 414, 429, 691, 716]
fer_ressource_1 = len(fer_x_1)
fer_go_out_0 = [979, 677]
fer_go_back_0 = [1511, 1073]
# Map 2
fer_x_2 = [1755, 1681, 1606, 1286, 1039, 996, 811, 729, 386, 315]
fer_y_2 = [798, 763, 734, 581, 558, 524, 602, 644, 818, 858]
fer_ressource_2 = len(fer_x_2)
fer_go_out_1 = [493, 905]
fer_go_back_1 = [1499, 1132]  # Map vide
# Map 3
fer_x_3 = [1551, 1481, 1408, 1274, 1192, 395, 327]
fer_y_3 = [644, 609, 576, 542, 582, 708, 750]
fer_ressource_3 = len(fer_x_3)
fer_go_out_2 = [686, 730]  # Map vide
fer_go_back_2 = [1635, 999]

#----Cuivre----
# Map 1
cuivre_x_1 = [525,448,525,784,863,1143,1268,1348,1534,1601]
cuivre_y_1 = [970,562,516,392,362,321,370,412,445,413]
cuivre_ressource_1 = len(cuivre_x_1)


# Map 2
cuivre_x_2 = [876,946]
cuivre_y_2 = [323,346]
cuivre_ressource_2 = len(cuivre_x_2)


# Map 3
cuivre_x_3 = [1883,1741,1632,1276,1123,1062,666,595,253,194]
cuivre_y_3 = [945,588,595,389,413,437,482,446,579,604]
cuivre_ressource_3 = len(cuivre_x_3)

cuivre_sortie_0 = [619, 561]
cuivre_sortie_1 = [562,530]
cuivre_retour_1 = [1984, 1245]
cuivre_retour_0 = [1578,1238]

minerai = input("Quel minerai à prendre ?")
mouvement(2264, 1268)

if minerai == "Fer" or minerai == "fer":
    while not keyboard.is_pressed('q'):
        time.sleep(random.uniform(0.2, 0.3))
        # Map 1
        for i in range(fer_ressource_1):
            recolte(fer_x_1[i], fer_y_1[i])
        # Map 1 - Sortie
        mouvement(fer_go_out_0[0], fer_go_out_0[1])
        time.sleep(6)
        # Map 2
        for i in range(fer_ressource_2):
            recolte(fer_x_2[i], fer_y_2[i])
        # Map 2 - Sortie
        mouvement(fer_go_out_1[0], fer_go_out_1[1])
        time.sleep(6)
        # Entree map vide
        mouvement(fer_go_out_2[0], fer_go_out_2[1])
        time.sleep(6)
        # Sorti map vide
        # Map 3
        for i in range(fer_ressource_3):
            recolte(fer_x_3[i], fer_y_3[i])
        # Map 3 - Sortie
        mouvement(fer_go_back_2[0], fer_go_back_2[1])
        time.sleep(6)
        # Map vide - Sortie
        mouvement(fer_go_back_1[0], fer_go_back_1[1])
        time.sleep(6)

        # Map 2
        for i in range(fer_ressource_2):
            recolte(fer_x_2[i], fer_y_2[i])

        mouvement(fer_go_back_0[0], fer_go_back_0[1])
        time.sleep(5)

        souris("Ressource/Inventaire.png")
        if pyautogui.locateOnScreen("Ressource/Alerte_full.png", confidence=0.8):
            souris("Ressource/Inventaire.png")
            sell("Ressource/Fer.png")
        else:
            souris("Ressource/Inventaire.png")

elif minerai == "Cuivre" or minerai == "cuivre":
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