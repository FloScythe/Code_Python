"""
Créer un bot :
	1. Lister les actions à effectuer manuellement
	2. Coder le programme en brut
	3. Repartir en fonction
"""
"""
		1.1 Déplacer le curseur sur le minerais
			1.1.1 Si detection du minerais
            1.1.2 Sinon retour sur 1.1
        1.2 Clique
		1.3 Attendre le temps de la récolte
        1.4 Boucler
            1.4.1 Si aucune detection
                1.4.1.1 Changer de map
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

liste_x = [-1464,-1386,-991,-943,-1663]
liste_y = [483,491,673,691,846]
ressource = 5


while keyboard.is_pressed('q') == False:
    time.sleep(random.uniform(0.1, 1))
    for i in range(ressource) :
        pyautogui.moveTo(liste_x[i], liste_y[i], duration=random.uniform(0.1, 0.5))
        pyautogui.click()
        time.sleep(random.uniform(0.1, 0.5))
