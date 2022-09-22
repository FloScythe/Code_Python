"""
		1.1 Déplacer le curseur sur le minerais
        1.2 Clique
        1.4 Boucler
        1.5 Combat
            Spam invoc

    ../Dossier/Nom.png
"""
import pyautogui
import random
import time
import keyboard


def souris(nom):
    z = pyautogui.locateOnScreen(nom, confidence=0.6)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(1)

"""
Deplacement 
Case de départ -> gauche -> gauche -> haut -> droite -> droite -> bas
(88,1066),(1675,69);(3021,1355);(1723,2065)
Marche pas des masse hein
"""

# gauche = [88,1066]
# haut = [1675,69]
# droite = [3021,1355]
# bas = [1723,2065]

while not keyboard.is_pressed('q'):
    souris("../Ressource/ble.png")

#wtf ce repop
# pas dispo?

