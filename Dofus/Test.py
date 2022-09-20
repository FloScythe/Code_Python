import pyautogui
import random
import time
import keyboard

# Chemin jusqu'a la mine
# for i in range(2):
#     pyautogui.moveTo(1013, 1169, duration=random.uniform(0.1, 0.3))
#     pyautogui.click()
#     time.sleep(4)
# for y in range(8):
#     pyautogui.moveTo(251, 626, duration=random.uniform(0.1, 0.3))
#     pyautogui.click()
#     time.sleep(6)
"""
Selectionner minerai
Si rien
    Clic
Si fenetre
    pass
Si
"""
def recolte(x,y):
    pyautogui.moveTo(x, y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    if pyautogui.locateOnScreen("Ressource/Fenetre_vide.png", confidence=0.7) :
        pass
    else :
        time.sleep(12)
    time.sleep(random.uniform(0.3,0.5))

def souris(nom):
    z = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(1)


# Map 1
liste_x_1 = [936, 1205, 1267, 1810, 1876]
liste_y_1 = [804, 414, 429, 691, 716]
ressource_1 = len(liste_x_1)
repos1 = 4 * random.uniform(12, 12.5)

# Map 2
liste_x_2 = [1755, 1681, 1606, 1286, 1039, 996, 811, 729, 386, 315]
liste_y_2 = [798, 763, 734, 581, 558, 524, 602, 644, 818, 858]
ressource_2 = len(liste_x_2)
repos2 = 4 * random.uniform(12, 12.5)

# Map 3
liste_x_3 = [1551, 1481, 1408, 1274, 1192, 395, 327]
liste_y_3 = [644, 609, 576, 542, 582, 708, 750]
ressource_3 = len(liste_x_3)
repos3 = 4 * random.uniform(12, 12.5)

# Trajet
go_out_0 = [979, 677]
go_out_1 = [493, 905]
go_out_2 = [686, 730]  # Map vide

go_back_2 = [1635, 999]
go_back_1 = [1499, 1132]  # Map vide
go_back_0 = [1511, 1073]

#Map1
# for i in range(ressource_1):
#     test(liste_x_1[i],liste_y_1[i])
# pyautogui.moveTo(go_out_0[0], go_out_0[1], duration=random.uniform(0.1, 0.3))
# pyautogui.click()
# time.sleep(5)

pyautogui.moveTo(go_back_2[0], go_back_2[1], duration=random.uniform(0.1, 0.3))
pyautogui.click()
time.sleep(5)