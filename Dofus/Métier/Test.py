import time
import keyboard
import pyautogui
import random
import unidecode


# -------------------------------
def clics(nom):
    if pyautogui.locateOnScreen(nom, confidence=0.8):
        position = pyautogui.locateOnScreen(nom, confidence=0.8)
        pyautogui.moveTo(position, duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        time.sleep(0.5)
    else:
        print("Clic non réalisé")


# -------------------------------
def doubleclics(nom):
    if pyautogui.locateOnScreen(nom, confidence=0.8):
        position = pyautogui.locateOnScreen(nom, confidence=0.8)
        pyautogui.moveTo(position, duration=random.uniform(0.1, 0.3))
        pyautogui.doubleClick()
        time.sleep(0.5)
    else:
        print("Double clic non réalisé")


# -------------------------------
def fenetre():
    while pyautogui.locateOnScreen("Ressource_Flo/Quit.png", confidence=0.8):
        clics("Ressource_Flo/Quit.png")
        break


# -------------------------------
def select(nom):
    # Verification de la présence du céréale
    selection = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(selection, duration=random.uniform(0.1, 0.3))
    print("")
    # Verifie si c'est récoltable
    pyautogui.mouseDown()
    time.sleep(0.5)
    vide = pyautogui.locateOnScreen("Ressource_Flo/vide.PNG", confidence=0.8)
    if vide:
        print("Pas disponible, au suivant")
        return
    elif not vide:
        pyautogui.mouseUp(duration=0.3)
        pyautogui.click()
        time.sleep(1)
        print(f"Récolte {cereale} : {i}")
        time.sleep(1)
        combat(2108, 416)
    else:

        pass


# -------------------------------
def deplacement(x,y):
    pyautogui.moveTo(x,y,duration=random.uniform(0.1,0.3))
    pyautogui.click()
    time.sleep(7)


# -------------------------------
def combat(x1, y1):
    if pyautogui.locateOnScreen("../Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "../Combat/Findetour.png", grayscale=True, confidence=0.8):
        clics("../Combat/Pret.png")
        print("Debut du mode combat")
        # Boucle infini :
        while True:
            """
                SI tofu dispo :
                    Choisir tofus
                    Choisir case bleu
                    Double clics
            """
            if pyautogui.pixelMatchesColor(x1, y1, (73, 97, 37)):
                clics("../Combat/invoc_tofu.png")
                doubleclics("../Combat/invoc2.png")
                clics("../Combat/Findetour.png")
                time.sleep(2)
            else:
                pyautogui.moveTo(pyautogui.locateOnScreen("../Combat/Deplacement.png", confidence=0.8),
                                 duration=random.uniform(0.1, 0.3))
                pyautogui.doubleClick(duration=0.5)
                clics("../Combat/Findetour.png")
                time.sleep(2)
            resume = pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8)
            dead = pyautogui.locateOnScreen("../Combat/dead.png", confidence=0.8)
            if resume and not dead:
                print("C'est gagné")
                print("Fin du mode combat")
                fenetre()
            elif resume and dead:
                print("T'es mort")
                pyautogui.moveTo(2753, 769)
                pyautogui.click()
                keyboard.send("ctrl+F2")
                time.sleep(1)
                print("Fin du mode combat")
    else:
        print("Pas de combat détecté")


# -------------------------------
def inventaire():
    if pyautogui.locateOnScreen("Ressource_Flo/Inventaire_Full.PNG"):
        clics("Ressource_Flo/Inventaire.PNG")
        print("Inventaire plein")
        return True
    else:
        if pyautogui.locateOnScreen("Ressource_Flo/Inventaire.PNG"):
            clics("Ressource_Flo/Inventaire.PNG")
            if pyautogui.locateOnScreen("Ressource_Flo/Alerte_full.PNG"):
                print("Inventaire presque plein")
                return True
            else:
                clics("Ressource_Flo/Inventaire.PNG")
                print("R.A.S")
                return False
        else:
            print("Pas de vente")
            return False


# -------------------------------
def vente(x):
    while True:
        clics("Ressource_Flo/Inventaire.png")
        clics("Ressource_Flo/Ressource_Inventaire.png")
        clics(x)
        clics("../Ressource/hdv.png")
        clics("../Ressource/QTE100.png")
        if pyautogui.locateOnScreen("../Ressource/Entrer.png", confidence=0.8):
            clics("../Ressource/Entrer.png")
            clics("../Ressource/Mettre_en_vente.png")
            clics("../Ressource/Vente.png")
            clics("../Combat/Quit.png")
            print(f"Mise en vente de : {x}")
        else:
            clics("../Combat/Quit.png")
            break


# -------------------------------
"""
--- Help ---
# Debut du programme :

"""
# -------------------------------
"""
Ordre d'execution :
Boucle infini 
1.  Verification    -- fenetre / combat / inventaire --OK
2.  Identification  -- Identifier le type de cereale --OK
3.  Selection       -- Selecionner le cereale
4   Validation      -- Verifier si le céréale est disponible
4.  Confirmation    -- Lancer la recolte
5.  Transition      -- Changement de map
"""

"""Verification avant programme
fenetre -- Si il n'y a aucune fenetre d'ouvert
combat --Si aucun combat n'est en cours
Inventaire -- Si il y'a de la place dans l'inventaire si non vendre
"""
cereale = input("Quel type de céréale ? ")
cereale = unidecode.unidecode(cereale)
cereale = cereale.lower()

print(f"Cereale choisi : {cereale}")

print("Demarrage du programme : ")
# Boucle Start

i = 0  # Verifie le nommbre d'iteration
# BOUCLE = 10  # Nombre de fois que la boucle tourne
LEVEL = 40  # Niveau métier actuel
temps = 12 - (10 * LEVEL / 100) + 1  # Temps de recolte

fenetre()
combat(2108, 416)
if inventaire():
    vente("Ressource_Flo/Ble_inventaire.png")
    vente("Ressource_Flo/Orge_inventaire.png")
    vente("Ressource_Flo/Avoine_inventaire.png")
    vente("Ressource_Flo/Houblon_inventaire.png")
    vente("Ressource_Flo/Lin_inventaire.png")

# -------------------------------
"""Identification du céréale
cereale = input("Quel type de céréale ? ")
Si blé :
    Selection
    Clic
"""

if cereale == "ble":
    select("Ressource_Flo/Ble.PNG")
    # # Selection du cereale
    # selection = pyautogui.locateOnScreen("Ressource_Flo/Ble.PNG", confidence=0.8)
    # pyautogui.moveTo(selection, duration=random.uniform(0.1, 0.3))
    # # Verifie si c'est récoltable
    # pyautogui.mouseDown()
    # time.sleep(0.5)
    # vide = pyautogui.locateOnScreen("Ressource_Flo/vide.PNG", confidence=0.8)
    # if not vide:
    #     pyautogui.mouseUp(duration=0.3)
    #     pyautogui.click()
    #     time.sleep(1)
    #     print(f"Récolte {cereale} : {i}")
    #     time.sleep(1)
    #     combat(2108, 416)
    # else:
    #     print("Pas disponible, au suivant")

elif cereale == "orge":
    select("Ressource_Flo/Orge.PNG")
elif cereale == "avoine":
    select("Ressource_Flo/Avoine.PNG")
elif cereale == "houblon":
    select("Ressource_Flo/Houblon.PNG")
elif cereale == "lin":
    select("Ressource_Flo/lin.PNG")
