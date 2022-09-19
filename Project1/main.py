"""
Créer un bot :
	1. Lister les actions à effectuer manuellement
	2. Coder le programme en brut
	3. Repartir en fonction
"""
"""
		1.1 Déplacer le curseur sur le minerais
        1.2 Clique
        1.4 Boucler
        1.5 Combat
            Spam invoc
            
"""
#Module de controle de la souris
import pyautogui
import random
import time
import keyboard

#Deplace le curseur au coordonnée x,y selon un temps donner
# pyautogui.moveTo(-100, 100, duration = random.uniform(0.1,0.9))

#Deplace le curseur selon son ancienne position
# pyautogui.moveRel(0, 50, duration = vitesse)

#pyautogui.click(100, 100)
# z = pyautogui.locateOnScreen('fer.png')
# pyautogui.moveTo(z,duration = vitesse)

#Map 1
liste_x_1 = [637,688,1078,1146,1319,1421,1473]
liste_y_1 = [689,661,487,455,437,456,546]
ressource_1 = len(liste_x_1)


while keyboard.is_pressed('q') == False:
    time.sleep(random.uniform(0.1, 0.5))
    for i in range(ressource_1) :
        pyautogui.moveTo(liste_x_1[i], liste_y_1[i], duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        time.sleep(random.uniform(0.1, 0.3))
