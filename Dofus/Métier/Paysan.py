import time
import keyboard
import pyautogui
import random
import unidecode


def clics(x, confidence):
    position = pyautogui.locateOnScreen(x, confidence=confidence)
    pyautogui.moveTo(position, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(0.5)


def fenetre():
    # Fenetre
    while pyautogui.locateOnScreen("Ressource_Flo/Quit.png", confidence=0.8):
        clics("Ressource_Flo/Quit.png", 0.8)


def sac():
    # Utilisation du sac de ressource
    clics("Ressource_Flo/Inventaire.PNG", 0.8)
    clics("Ressource_Flo/sac_de_ressource.PNG", 0.7)
    pyautogui.click()
    clics("Ressource_Flo/Quit.png", 0.7)
    time.sleep(0.5)


def combat(x, y):
    # Combat
    if pyautogui.locateOnScreen("../Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "../Combat/Findetour.png", grayscale=True, confidence=0.8):
        clics("../Combat/Pret.png", 0.8)

        print("Debut du mode combat")
        # Boucle infini :
        while True:
            match = pyautogui.pixelMatchesColor(x, y, (73, 97, 37))
            if match:
                while match:
                    clics("../Combat/invoc_tofu.png", 0.8)
                    clics("../Combat/invoc2.png", 0.8)
                    pyautogui.click()
                    match = pyautogui.pixelMatchesColor(x, y, (73, 97, 37))

                clics("../Combat/Findetour.png", 0.8)
                time.sleep(3)

            elif not match:
                pyautogui.moveTo(pyautogui.locateOnScreen("../Combat/Deplacement.png", confidence=0.8),
                                 duration=random.uniform(0.1, 0.3))
                pyautogui.doubleClick(duration=0.5)
                clics("../Combat/Findetour.png", 0.8)
                pyautogui.click()
                time.sleep(3)

            resume = pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8)
            dead = pyautogui.locateOnScreen("Ressource_Flo/dead.png", confidence=0.8)
            if resume and not dead:
                print("C'est gagné")
                print("Fin du mode combat")
                clics("Ressource_Flo/Quit.png", 0.8)
                sac()
                return

            elif dead:
                print("T'es mort")
                pyautogui.moveTo(2753, 769)
                pyautogui.click()
                keyboard.send("ctrl+F2")
                time.sleep(1)
                print("Fin du mode combat")
                return
    else:
        print("Pas de combat détecté")


def inventaire():
    # ----- Check de l'inventaire -----
    clics("Ressource_Flo/Inventaire.PNG", 0.8)

    if pyautogui.locateOnScreen("Ressource_Flo/Alerte_full.PNG", confidence=0.8):
        clics("Ressource_Flo/Inventaire.PNG", 0.8)
        print("Inventaire presque plein ou plein")
        return True
    else:
        clics("Ressource_Flo/Inventaire.PNG", 0.8)
        print("R.A.S")
        return False


def verification():
    fenetre()
    combat(2108, 416)


def vente(x):
    # ----- Vente -----
    for i in range(2):
        clics("Ressource_Flo/Inventaire.PNG", 0.8)
        clics("Ressource_Flo/Ressource_Inventaire.png", 0.8)
        if pyautogui.locateOnScreen(x, confidence=0.65):
            clics(x, 0.7)
            clics("../Ressource/hdv.png", 0.8)
            clics("../Ressource/QTE100.png", 0.8)
        else:
            clics("Ressource_Flo/Quit.PNG", 0.8)
            return
        if pyautogui.locateOnScreen("../Ressource/Entrer.png", confidence=0.8):
            clics("../Ressource/Entrer.png", 0.8)
            clics("../Ressource/Mettre_en_vente.png", 0.8)
            clics("../Ressource/Vente.png", 0.8)
            clics("../Combat/Quit.png", 0.8)
        else:
            clics("Ressource_Flo/Quit.PNG", 0.8)
            return


def recolte(x):
    for i in range(10):
        action = False
        combat(2108, 416)
        fenetre()
        localisation = pyautogui.locateOnScreen(x, confidence=0.7)
        pyautogui.moveTo(localisation)
        if localisation:
            pyautogui.mouseDown()
            action = True

        non_disponible = pyautogui.locateOnScreen("Ressource_Flo/non_disponible.PNG", confidence=0.95)
        time.sleep(1)

        # ---- Cereale disponible ----
        if localisation and not non_disponible:
            print("Le céréale peut etre récupéré")
            pyautogui.click()
            action = True
            time.sleep(1)

        # # ---- Cereale non disponible ----
        # elif localisation and non_disponible:
        #     print("Le céréale est déjà pris")
        #     action = True
        #
        # if not action:
        #     time.sleep(temps)
        #     print("Il faut changer de carte")
        #     # ----- Controle des cartes de récolte -----
        #     map1 = pyautogui.locateOnScreen("Ressource_Flo/Map1.png")
        #     map2 = pyautogui.locateOnScreen("Ressource_Flo/Map2.png")
        #     map3 = pyautogui.locateOnScreen("Ressource_Flo/Map3.png")
        #     if map1:
        #         print("Carte actuelle : 1")
        #         print("Changement de map")
        #         pyautogui.mouseUp()
        #         deplacement_bas()
        #     elif map2:
        #         print("Carte actuelle : 2")
        #         print("Changement de map")
        #         pyautogui.mouseUp()
        #         deplacement_bas()
        #         deplacement_gauche()
        #     elif map3:
        #         print("Carte actuelle : 3")
        #         print("Changement de map")
        #         pyautogui.mouseUp()
        #         deplacement_haut()
        #         deplacement_haut()
        #         deplacement_droite()


def deplacement_haut():
    pyautogui.moveTo(1050, 55, duration=random.uniform(0.2, 0.3))
    pyautogui.click()
    time.sleep(6)


def deplacement_bas():
    pyautogui.moveTo(1700, 1375, duration=random.uniform(0.2, 0.3))
    pyautogui.click()
    time.sleep(6)


def deplacement_droite():
    pyautogui.moveTo(2025, 520, duration=random.uniform(0.2, 0.3))
    pyautogui.click()
    time.sleep(6)


def deplacement_gauche():
    pyautogui.moveTo(105, 520, duration=random.uniform(0.2, 0.3))
    pyautogui.click()
    time.sleep(6)


ble = "Ressource_Flo/Ble.PNG"
orge = "Ressource_Flo/Orge.PNG"
avoine = "Ressource_Flo/Avoine.PNG"
houblon = "Ressource_Flo/Houblon.PNG"
lin = "Ressource_Flo/Lin.PNG"
seigle = "Ressource_Flo/Seigle.PNG"
malt = "Ressource_Flo/Malt.PNG"

print("Demarrage du programme : ")
cereale = input("Quel type de céréale ? ")
cereale = unidecode.unidecode(cereale)
cereale = cereale.lower()

print(f"Cereale choisi : {cereale}")
level = 64  # Niveau métier actuel
temps = 12 - (10 * level / 100)  # Temps de recolte

# Verification de l'écran
verification()

while True:
    # Vérification de l'inventaire
    if inventaire():
        if cereale == "ble":
            vente("Ressource_Flo/Ble_inventaire.PNG")
        elif cereale == "orge":
            vente("Ressource_Flo/Orge_inventaire.PNG")
        elif cereale == "avoine":
            vente("Ressource_Flo/Avoine_inventaire.PNG")
        elif cereale == "houblon":
            vente("Ressource_Flo/Houblon_inventaire.PNG")
        elif cereale == "lin":
            vente("Ressource_Flo/Lin_inventaire.PNG")
        elif cereale == "seigle":
            vente("Ressource_Flo/Seigle_inventaire.PNG")
        elif cereale == "malt":
            vente("Ressource_Flo/Malt_inventaire.PNG")
        else:
            print("Hors catégorie")

    if cereale == "ble":
        recolte(ble)
    elif cereale == "orge":
        recolte(orge)
    elif cereale == "avoine":
        recolte(avoine)
    elif cereale == "houblon":
        recolte(houblon)
    elif cereale == "lin":
        recolte(lin)
    elif cereale == "seigle":
        recolte(seigle)
    elif cereale == "malt":
        recolte(malt)
