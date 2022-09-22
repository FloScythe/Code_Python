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

from Function import souris



while keyboard.is_pressed('q') == False:
    time.sleep(random.uniform(0.1, 0.5))
    # for i in range(ressource_1):
        # pyautogui.moveTo(liste_x_1[i], liste_y_1[i], duration=random.uniform(0.1, 0.3))
        # pyautogui.click()
        # time.sleep(random.uniform(0.1, 0.3))
    if pyautogui.locateOnScreen("../Ressource/ble.png",confidence=0.6):
        souris("../Ressource/ble.png")

