import pyautogui
import random
import time
import keyboard

# Chemin jusqu'a la mine
# for i in range(2):
#     pyautogui.moveTo(1013, 1169, duration=random.uniform(0.1, 0.3))
#     pyautogui.click()
#     time.sleep(4)
# for y in range(8):
#     pyautogui.moveTo(251, 626, duration=random.uniform(0.1, 0.3))
#     pyautogui.click()
#     time.sleep(6)
"""
Ouvrir l'inventaire
Selectionner la ressource
Selectionner hdv
Bouton quantité x100
Bouton mettre en vente
Vendre
Quitter
"""


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

souris("Ressource/Inventaire.png")
if pyautogui.locateOnScreen("Ressource/Alerte_full.png", confidence=0.8):
    souris("Ressource/Inventaire.png")
    sell()
else:
    souris("Ressource/Inventaire.png")