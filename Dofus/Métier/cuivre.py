import pyautogui
import random
import time
import keyboard

from Code_Python.Dofus.Function import recolte, mouvement, souris, sell

# ----Cuivre----

def map3_9_1():
    cuivre_x_1 = [525, 448, 525, 784, 863, 1143, 1268, 1348, 1534, 1601]
    cuivre_y_1 = [970, 562, 516, 392, 362, 321, 370, 412, 445, 413]
    cuivre_ressource_1 = len(cuivre_x_1)

    for i in range(cuivre_ressource_1):
        recolte(cuivre_x_1[i], cuivre_y_1[i])


def map3_9_2():
    cuivre_x_2 = [876, 946]
    cuivre_y_2 = [323, 346]
    cuivre_ressource_2 = len(cuivre_x_2)
    for i in range(cuivre_ressource_2):
        recolte(cuivre_x_2[i], cuivre_y_2[i])


def map3_9_3():
    cuivre_x_3 = [1883, 1741, 1632, 1276, 1123, 1062, 666, 595, 253, 194]
    cuivre_y_3 = [945, 588, 595, 389, 413, 437, 482, 446, 579, 604]
    cuivre_ressource_3 = len(cuivre_x_3)
    for i in range(cuivre_ressource_3):
        recolte(cuivre_x_3[i], cuivre_y_3[i])


cuivre_sortie_0 = [602, 558]
cuivre_sortie_1 = [533, 528]
cuivre_retour_1 = [2005, 1250]
cuivre_retour_0 = [1595, 1252]

while not keyboard.is_pressed('q'):
    time.sleep(random.uniform(0.2, 0.3))
    # Map 1
    map3_9_1()
    # Map 1 - Sortie
    mouvement(cuivre_sortie_0[0], cuivre_sortie_0[1])
    time.sleep(6)
    # Map 2
    map3_9_2()
    # Map 2 - Sortie
    mouvement(cuivre_sortie_1[0], cuivre_sortie_1[1])
    time.sleep(6)
    # Map 3
    map3_9_3()
    # Map 3 - Sortie
    mouvement(cuivre_retour_1[0], cuivre_retour_1[1])
    time.sleep(6)
    # Map 2
    map3_9_2()
    # Map 2 - Sortie
    mouvement(cuivre_retour_0[0], cuivre_retour_0[1])
    time.sleep(6)

    souris("../Ressource/Inventaire.png")
    if pyautogui.locateOnScreen("../Ressource/Alerte_full.png", confidence=0.8):
        souris("../Ressource/Inventaire.png")
        sell("../Ressource/Cuivre.png")
    else:
        souris("../Ressource/Inventaire.png")
