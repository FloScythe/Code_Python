import pyautogui
import random
import time
import keyboard

import pyautogui

from Code_Python.Dofus.Function import recolte, mouvement, souris, sell, level_up


# # ---- Bronze ----
#
def map3_9_1(a,b):
    x_1 = [378, 523, 588, 663, 805, 856, 1047, 1130, 1194, 1325, 1397, 1680]
    y_1 = [998, 922, 903, 853, 791, 758, 680, 630, 596, 534, 502, 457]
    ressource_1 = len(x_1)

    for i in range(ressource_1):
        recolte(x_1[i], y_1[i],a,b)


def map3_9_2(a,b):
    x_2 = [430, 514,654, 643,  707, 833, 907, 1042, 1167, 1333, 1477, 1552, 1616, 1688]
    y_2 = [976, 914, 872, 679, 635, 577, 557, 496, 487, 549, 617, 656, 755, 798]
    ressource_2 = len(x_2)
    for i in range(ressource_2):
        recolte(x_2[i], y_2[i],a,b)


aller_0 = [459, 1192]
aller_1 = [467, 903]
aller_2 = [1540, 709]
retour_3 = [516, 1154]
retour_4 = [1529, 1146]
retour_5 = [1475, 732]

while not keyboard.is_pressed('q'):
    # Map 1
    map3_9_1(2108,415)
    level_up()
    # Map 1 - Sortie
    mouvement(aller_0[0], aller_0[1])
    time.sleep(random.uniform(5,6))
    #Chemin
    mouvement(aller_1[0], aller_1[1])
    time.sleep(random.uniform(5,6))
    mouvement(aller_2[0], aller_2[1])
    time.sleep(random.uniform(5,6))
    # Map 2
    map3_9_2(2108,415)
    level_up()
    # Map 2 - Sortie
    mouvement(retour_3[0], retour_3[1])
    time.sleep(random.uniform(5,6))
    #Chemin
    mouvement(retour_4[0], retour_4[1])
    time.sleep(random.uniform(5,6))
    mouvement(retour_5[0], retour_5[1])
    time.sleep(random.uniform(5,6))

    souris("../Ressource/Inventaire.png")
    if pyautogui.locateOnScreen("../Ressource/sac_bronze.png", confidence=0.8):
        z = pyautogui.locateOnScreen("../Ressource/sac_bronze.png", confidence=0.8)
        pyautogui.moveTo(z,duration=random.uniform(0.1, 0.3))
        pyautogui.click(clicks=2)
    elif pyautogui.locateOnScreen("../Ressource/Parchemin_mineur.png", confidence=0.8):
        z = pyautogui.locateOnScreen("../Ressource/sac_bronze.png", confidence=0.8)
        pyautogui.moveTo(z,duration=random.uniform(0.1, 0.3))
        pyautogui.click(clicks=2)
    else:
        souris("../Ressource/Inventaire.png")

    souris("../Ressource/Inventaire.png")
    if pyautogui.locateOnScreen("../Ressource/Alerte_full.png", confidence=0.8):
        souris("../Ressource/Inventaire.png")
        sell("../Ressource/Bronze.png")
    else:
        souris("../Ressource/Inventaire.png")
