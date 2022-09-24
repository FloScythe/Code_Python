import time
import keyboard
import pyautogui
import random

"""
# Debut du programme :
i = 0 -- Verifie le nommbre d'iteration
BOUCLE = 10 --Nombre de fois que la boucle tourne
LEVEL = 40 -- Niveau métier actuel
temps = 12 - (10 * LEVEL / 100) + 1 -- Temps de recolte
"""
print("Demarrage du programme : ")
"""
Ordre d'execution :
1.  Verification    -- fenetre / combat / inventaire
2.  Identification     -- Identifier le type de cereale
3.  Selection   -- Selecionner le cereale
4.  Validation  -- Lancer la recolte
5.  Transition  --  Changement de map
"""


# -------------------------------
def clics(nom):
    position = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(position, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(0.5)


def doubleclics(nom):
    position = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(position, duration=random.uniform(0.1, 0.3))
    pyautogui.doubleClick()
    time.sleep(0.5)


def fenetre():
    while pyautogui.locateOnScreen("Ressource_Flo/Quit.png", confidence=0.8):
        clics("Ressource_Flo/Quit.png")


# -------------------------------
def combat(x1, y1):
    if pyautogui.locateOnScreen("../Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "../Combat/Findetour.png", grayscale=True, confidence=0.8):
        clics("../Combat/Pret.png")
        print("Debut du mode combat")
    """
    Boucle infini :
    """
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
        if resume and dead:
            print("T'es mort")
            pyautogui.moveTo(2753, 769)
            pyautogui.click()
            keyboard.send("ctrl+F2")
            time.sleep(1)
            print("Fin du mode combat")
        elif resume and not dead:
            print("C'est gagné")
            print("Fin du mode combat")
            fenetre()


# -------------------------------
def inventaire():
    pass

# -------------------------------
"""
# Verification avant programme
fenetre -- Si il n'y a aucune fenetre d'ouvert
combat --Si aucun combat n'est en cours
Inventaire -- Si il y'a de la place dans l'inventaire si non vendre
"""

fenetre()
combat(

)