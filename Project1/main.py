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

liste_x = [472,579,636,693,784,838,1001,1055,1091,1205,1255,1460]
liste_y = [876,823,799,767,719,689,604,580,578,499,465,471]
ressource = 11


while keyboard.is_pressed('q') == False:
    time.sleep(random.uniform(0.1, 0.5))
    for i in range(ressource+1) :
        pyautogui.moveTo(liste_x[i], liste_y[i], duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        time.sleep(random.uniform(0.1, 0.3))
