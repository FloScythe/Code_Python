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
liste_x_1 = [1737,1895,1516,1431,1358,1267,1075,1255,1351,1770,1755,1839,2090,2236,2355,1870,1800]
liste_y_1 = [777,758,1000,1043,1085,1041,1264,1449,1493,1612,1699,1740,1454,1363,1477,1338,1231]
ressource_1 = len(liste_x_1)


while not keyboard.is_pressed('q'):
    time.sleep(random.uniform(0.1, 0.5))
    for i in range(ressource_1):
        pyautogui.moveTo(liste_x_1[i], liste_y_1[i], duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        time.sleep(random.uniform(0.1, 0.3))