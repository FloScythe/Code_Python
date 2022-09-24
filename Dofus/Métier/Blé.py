# Programme de Paysan

"""
Deplacer le curseur par reconnaissance d'image
Cliquer sur le blé
Attendre moins que le temps de recolte
Relancer la boucle
1.Si la carte est vide
    Verifier si l'inventaire est plein
    Vendre si plein
    Bouger de carte
"""
import time

import keyboard
import pyautogui
import random


def souris(nom):
    z = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(0.5)


def level_up():
    # Detection en cas de level up
    time.sleep(1)
    if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
        up = pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8)
        pyautogui.moveTo(up, duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        print(f"Level up !")


def combat(x3, y3):
    if pyautogui.locateOnScreen("../Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "../Combat/Findetour.png", grayscale=True, confidence=0.8):

        souris("../Combat/Pret.png")
        print("Debut du combat")

        while True:
            if pyautogui.pixelMatchesColor(x3, y3, (73, 97, 37)):
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
                if pyautogui.locateOnScreen("../Combat/dead.png", confidence=0.8):
                    print("T'es mort")
                    pyautogui.moveTo(2753, 769)
                    pyautogui.click()
                    keyboard.send("ctrl+F2")
                    time.sleep(1)
                souris("../Combat/Quit.png")
                time.sleep(1)
                if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
                    print("Fin du combat")
                    level_up()
                souris("../Ressource/Inventaire.png")
                z = pyautogui.locateOnScreen("Ressource_Flo/sac_houblon.png", confidence=0.8)
                pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
                pyautogui.doubleClick()
                souris("../Combat/Quit.png")
                break
        else:
            print("Pas de combat detecté")


def sell(x):
    souris("Ressource_Flo/Inventaire.png")
    souris("Ressource_Flo/Ressource_Inventaire.png")
    souris(x)
    souris("../Ressource/hdv.png")
    souris("../Ressource/QTE100.png")
    if pyautogui.locateOnScreen("../Ressource/Entrer.png", confidence=0.8):
        souris("../Ressource/Entrer.png")
        souris("../Ressource/Mettre_en_vente.png")
        souris("../Ressource/Vente.png")
        souris("../Combat/Quit.png")
    else:
        souris("../Combat/Quit.png")


i = 0
BOUCLE = 10
LEVEL = 35
temps = 12 - (10 * LEVEL / 100) + 1
print("Demarrage du programme : ")
while True:
    for nombre in range(BOUCLE):
        # ----Detection de combat en cours----
        combat(2108, 416)
        pyautogui.moveTo(1500, 720, duration=random.uniform(0.1,0.2))

        # ----Verification inventaire----
        if nombre == BOUCLE:
            while pyautogui.locateOnScreen("Ressource_Flo/Alerte_full.PNG"):
                # sell("Ressource_Flo/Ble_inventaire.png")
                # sell("Ressource_Flo/Orge_inventaire.png")
                # sell("Ressource_Flo/Avoine_inventaire.png")
                sell("Ressource_Flo/Houblon_inventaire.png")
        elif not nombre == BOUCLE:
            print("Rien a vendre")

        # ----Identification----
        ble = pyautogui.locateOnScreen("Ressource_Flo/Ble.PNG", confidence=0.7)
        orge = pyautogui.locateOnScreen("Ressource_Flo/Orge.PNG", confidence=0.7)
        avoine = pyautogui.locateOnScreen("Ressource_Flo/Avoine.PNG", confidence=0.7)
        houblon = pyautogui.locateOnScreen("Ressource_Flo/Houblon.PNG", confidence=0.7)
        coupe1 = pyautogui.locateOnScreen("Ressource_Flo/Ble_coupe.PNG", confidence=0.6)
        # coupe2 = pyautogui.locateOnScreen("Ressource_Flo/Orge_coupe.PNG", confidence=0.6)
        coupe3 = pyautogui.locateOnScreen("Ressource_Flo/Avoine_coupe.PNG", confidence=0.6)
        coupe4 = pyautogui.locateOnScreen("Ressource_Flo/Houblon_coupe.PNG", confidence=0.6)


        # ----Détection de la récolte----
        print("Selection du céréales")
        pyautogui.moveTo(ble or orge or avoine or houblon)
        pyautogui.mouseDown()
        time.sleep(random.uniform(0.1,0.2))
        vide = pyautogui.locateOnScreen("Ressource_Flo/vide.PNG", confidence=0.8)

        # ----Lancement de la récolte----
        if ble and not vide:
            i += 1
            print(f"Recolte Blé : {i}")
            pyautogui.click()
            time.sleep(temps)
            pyautogui.mouseUp()
            level_up()
            combat(2108, 416)
        elif orge and not vide:
            i += 1
            print(f"Recolte Orge : {i}")
            pyautogui.click()
            time.sleep(temps)
            pyautogui.mouseUp()
            level_up()
            combat(2108, 416)
        elif avoine and not vide:
            i += 1
            print(f"Recolte Avoine : {i}")
            pyautogui.click()
            time.sleep(temps)
            pyautogui.mouseUp()
            level_up()
            combat(2108, 416)
        elif houblon and not vide:
            i += 1
            pyautogui.mouseUp()
            pyautogui.click()
            time.sleep(temps)
            print(f"Recolte Houblon : {i}")
            level_up()
            combat(2108, 416)
        elif coupe1 or coupe3 or coupe4 or vide:
            pyautogui.mouseUp()
            houblon = pyautogui.locateOnScreen("Ressource_Flo/Houblon.PNG", confidence=0.7)
            pyautogui.moveTo(houblon)
            if houblon:
                print("Erreur, Selection nouveau céréale")

            # ----Changement de carte----
            map1 = pyautogui.locateOnScreen("Ressource_Flo/Map1.PNG", confidence=0.8)
            # map2 = pyautogui.locateOnScreen("Ressource_Flo/Map2.PNG", confidence=0.8)
            # map3 = pyautogui.locateOnScreen("Ressource_Flo/Map3.PNG", confidence=0.8)
            if not houblon:
                print("Rien trouvé")
                pyautogui.moveTo(1500,720)
                pyautogui.mouseUp()
                if map1:
                    print("Map 1")
                    for carte in range(5):
                        pyautogui.moveTo(2045, 720)
                        pyautogui.click()
                        time.sleep(7)
                    print("Changement de carte")
                elif not map1:
                    print("Map 2")
                    for carte in range(5):
                        pyautogui.moveTo(90, 720)
                        pyautogui.click()
                        time.sleep(7)
                    print("Changement de carte")

