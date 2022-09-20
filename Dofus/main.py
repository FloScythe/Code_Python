import random
import time
import pyautogui


def souris(nom):
    z = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(1)


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
sell("../Ressource/Cuivre.png")