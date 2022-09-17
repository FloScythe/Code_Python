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


vitesse = random.uniform(0.1,0.9)

time .sleep(1)
#Deplace le curseur au coordonnée x,y selon un temps donner
pyautogui.moveTo(100, 100, duration = vitesse)

#Deplace le curseur selon son ancienne position
# pyautogui.moveRel(0, 50, duration = vitesse)

#pyautogui.click(100, 100)
# z = pyautogui.locateOnScreen('fer.png')
# pyautogui.moveTo(z,duration = vitesse)

liste_x = [-1477,-1404,-986,-948,-1679]
liste_y = [473,485,683,704,722]
ressource = 5

switch = True
while switch:
    time.sleep(random.uniform(0.1, 1))
    if keyboard.is_pressed('q'):
        switch = False
        break
    else :
        for i in range(ressource) :
            pyautogui.moveTo(liste_x[i], liste_y[i], duration=random.uniform(0.1, 0.5))
            pyautogui.click()
            time.sleep(random.uniform(0.1, 0.5))
            if keyboard.is_pressed('q'):
                switch = False
                break
