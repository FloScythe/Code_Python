"""
		1.1 Déplacer le curseur sur le minerais
        1.2 Clique
        1.4 Boucler
        1.5 Combat
            Spam invoc
"""
import pyautogui
import random
import time
import keyboard

#Map 1
liste_x_1 = [637,688,1078,1146,1319,1421,1473]
liste_y_1 = [689,661,487,455,437,456,546]
ressource_1 = len(liste_x_1)

#Map 2
liste_x_2 = [637,688,1078,1146,1319,1421,1473]
liste_y_2 = [689,661,487,455,437,456,546]
ressource_2 = len(liste_x_2)

#Map 3
liste_x_3 = [637,688,1078,1146,1319,1421,1473]
liste_y_3 = [689,661,487,455,437,456,546]
ressource_3 = len(liste_x_3)

while keyboard.is_pressed('q') == False:
    time.sleep(random.uniform(0.1, 0.5))
    for i in range(ressource_1) :
        pyautogui.moveTo(liste_x_1[i], liste_y_1[i], duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        time.sleep(random.uniform(0.1, 0.3))
