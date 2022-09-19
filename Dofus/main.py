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
liste_x_1 = [895,1100,1161,1563,1616]
liste_y_1 = [726,430,457,637,665]
ressource_1 = len(liste_x_1)

#Map 2
liste_x_2 = [1159,1002,942,735,487,42]
liste_y_2 = [538,480,513,621,739,764]
ressource_2 = len(liste_x_2)

#Map 3
liste_x_3 = [1356,1305,1265,1138,1083,501,434]
liste_y_3 = [589,568,554,526,562,645,677]
ressource_3 = len(liste_x_3)

while keyboard.is_pressed('q') == False:
    time.sleep(random.uniform(0.1, 0.5))
    #Map 1
    for repetitions_1 in range(2):
        for i in range(ressource_1) :
            pyautogui.moveTo(liste_x_1[i], liste_y_1[i], duration=random.uniform(0.1, 0.3))
            pyautogui.click()
            time.sleep(random.uniform(0.1, 0.3))
    if keyboard.is_pressed('q'):
        print("Interruption de la boucle")
        break
    #Map 2
    for repetitions_2 in range(2):
        for i in range(ressource_1) :
            pyautogui.moveTo(liste_x_2[i], liste_y_2[i], duration=random.uniform(0.1, 0.3))
            pyautogui.click()
            time.sleep(random.uniform(0.1, 0.3))
    if keyboard.is_pressed('q'):
        print("Interruption de la boucle")
        break
    #Map 3
    for repetitions_3 in range(2):
        for i in range(ressource_1) :
            pyautogui.moveTo(liste_x_3[i], liste_y_3[i], duration=random.uniform(0.1, 0.3))
            pyautogui.click()
            time.sleep(random.uniform(0.1, 0.3))