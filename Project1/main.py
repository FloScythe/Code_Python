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

vitesse = random.uniform(0.1,0.9)

time .sleep(3)
#Deplace le curseur au coordonnée x,y selon un temps donner
print(vitesse)
pyautogui.moveTo(100, 100, duration = vitesse)

#Deplace le curseur selon son ancienne position
# pyautogui.moveRel(0, 50, duration = vitesse)

#pyautogui.click(100, 100)
z = pyautogui.locateOnScreen('Test.png')
pyautogui.moveTo(z,duration = vitesse)


switch = True
while switch:
    print(pyautogui.position())
    time.sleep(2)
