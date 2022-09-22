# Programme de minage
"""
Action à réaliser
- Positionner le curseur sur le minerai
- Faire un clic long sur le minerai
- Detecter Si in n'y a pas de croix
- Cliquer
"""
import pyautogui
import random
import time
import keyboard


def souris(nom):
    z = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(0.5)


def level_up():
    # Detection en cas de level up
    if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
        up = pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8)
        pyautogui.moveTo(up, duration=random.uniform(0.1, 0.3))
        pyautogui.click()


def combat(x1, y1, x2, y2, x3, y3):
    if pyautogui.locateOnScreen("../Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "../Combat/Findetour.png", grayscale=True, confidence=0.8):

        souris("../Combat/Pret.png")

        while True:
            if pyautogui.pixelMatchesColor(x1, y1, (73, 97, 37)):
                souris("../Combat/invoc_sanglier.png")
                souris("../Combat/invoc2.png")
                pyautogui.click()
            elif pyautogui.pixelMatchesColor(x2, y2, (46, 93, 107)):
                souris("../Combat/invoc_bouf.png")
                souris("../Combat/invoc2.png")
                pyautogui.click()
            elif pyautogui.pixelMatchesColor(x3, y3, (73, 97, 37)):
                souris("../Combat/invoc_tofu.png")
                souris("../Combat/invoc2.png")
                pyautogui.click()
            else:
                z = pyautogui.locateOnScreen("../Combat/Deplacement.png", confidence=0.8)
                pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
                pyautogui.doubleClick()
                time.sleep(0.5)
                souris("../Combat/Findetour.png")
                time.sleep(1)

            if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
                if pyautogui.locateOnScreen("../Combat/dead.png", confidence=0.8):
                    pyautogui.moveTo(2753,769)
                    pyautogui.click()
                    keyboard.send("ctrl+F2")
                    time.sleep(1)
                souris("../Combat/Quit.png")
                time.sleep(1)
                if pyautogui.locateOnScreen("../Combat/Quit.png", confidence=0.8):
                    level_up()
                souris("../Ressource/Inventaire.png")
                souris("../Ressource/sac.png")
                pyautogui.click()
                break
            elif keyboard.is_pressed("q"):
                time.sleep(1)
                break



def minage(a, b):
    pyautogui.moveTo(a[0], b[0])
    pyautogui.mouseDown()
    time.sleep(1)
    for i in range(len(a)):
        print(f"Minerai n° : {i + 1}")
        if not pyautogui.locateOnScreen("../Ressource/Mine.png", confidence=0.8):
            print("Trouvé")
            pyautogui.mouseUp()
            pyautogui.doubleClick()
            time.sleep(5 + 11)
            level_up()
            combat(2109, 421, 2099, 329, 2107, 890)
            pyautogui.moveTo(a[i], b[i], duration=random.uniform(0.2, 0.3))
            time.sleep(0.5)
            pyautogui.mouseDown()
            time.sleep(1)
        else:
            print("Rien")
            if i == len(a) - 1:
                pass
            else:
                pyautogui.moveTo(a[i + 1], b[i + 1], duration=random.uniform(0.1, 0.2))
            time.sleep(0.5)
    pyautogui.mouseUp()
    print("Carte terminé")
    souris("../Ressource/Inventaire.png")
    if pyautogui.locateOnScreen("../Ressource/Alerte_full.png", confidence=0.8):
        souris("../Ressource/Inventaire.png")
        sell("../Ressource/Fer.png")
        sell("../Ressource/Cuivre.png")
        sell("../Ressource/Bronze.png")
    else:
        souris("../Combat/Quit.png")


def deplacement(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    time.sleep(6)


def sell(x):
    souris("../Ressource/Inventaire.png")
    souris("../Ressource/Ressource_Inventaire.png")
    souris(x)
    souris("../Ressource/hdv.png")
    souris("../Ressource/QTE100.png")
    if pyautogui.locateOnScreen("../Ressource/Entrer.png", confidence=0.8):
        souris("../Ressource/Entrer.png")
        souris("../Ressource/Mettre_en_vente.png")
        souris("../Ressource/Vente.png")
        souris("../Combat/Quit.png")
    else:
        souris("../Combat/Quit.png")


# Fer1
x_1 = [936, 1205, 1267, 1810, 1876]
y_1 = [804, 414, 429, 691, 716]
# Fer2
x_2 = [1755, 1681, 1606, 1286, 1039, 996, 811, 729, 386, 315]
y_2 = [798, 763, 734, 581, 558, 524, 602, 644, 818, 858]
# Bronze1
x_3 = [378, 523, 588, 663, 805, 856, 1047, 1130, 1194, 1325, 1397, 1680]
y_3 = [998, 922, 903, 853, 791, 758, 680, 630, 596, 534, 502, 457]
# Bronze2
x_5 = [430, 514, 654, 643, 707, 833, 907, 1042, 1167, 1333, 1477, 1552, 1616, 1688]
y_5 = [976, 914, 872, 679, 635, 577, 557, 496, 487, 549, 617, 656, 755, 798]
# Fer3
x_6 = [1551, 1481, 1408, 1274, 1192, 395, 327]
y_6 = [644, 609, 576, 542, 582, 708, 750]
# Cuivre1
x_7 = [380, 455, 786, 850, 948, 1021, 1686, 1747, 1821]
y_7 = [931, 889, 451, 420, 408, 450, 653, 675, 717]
# Cuivre2
x_8 = [525, 448, 525, 784, 863, 1143, 1268, 1348, 1534, 1601]
y_8 = [970, 562, 516, 392, 362, 321, 370, 412, 445, 413]
# Cuivre3
x_9 = [876, 946]
y_9 = [323, 346]
# Cuivre4
x_10 = [1883, 1741, 1632, 1276, 1123, 1062, 666, 595, 253, 194]
y_10 = [945, 588, 595, 389, 413, 437, 482, 446, 579, 604]

while not keyboard.is_pressed('q'):
    minage(x_1, y_1)
    # ----------
    deplacement(979, 677)
    # ----------
    minage(x_2, y_2)
    # ----------
    deplacement(1475, 732)
    # ----------
    minage(x_3, y_3)
    # ----------
    deplacement(459, 1192)
    # ----------
    minage(x_2, y_2)
    # ----------
    deplacement(467, 903)
    deplacement(1540, 709)
    # ----------
    minage(x_5, y_5)
    # ----------
    deplacement(516, 1154)
    deplacement(686, 730)
    # ----------
    minage(x_6, y_6)
    # ----------
    deplacement(1635, 999)
    deplacement(1499, 1132)
    # ----------
    minage(x_2, y_2)
    # ----------
    deplacement(1511, 1073)
    # ----------
    minage(x_1, y_1)
    # ----------
    deplacement(1629, 665)
    deplacement(1908, 452)
    # ----------
    minage(x_7, y_7)
    # ----------
    deplacement(1546, 632)
    deplacement(1553, 305)
    # ----------
    minage(x_8, y_8)
    # ----------
    deplacement(566, 530)
    # ----------
    minage(x_9, y_9)
    # ----------
    deplacement(566, 530)
    # ----------
    minage(x_10, y_10)
    # ----------
    deplacement(2014, 1269)
    # ----------
    minage(x_9, y_9)
    # ----------
    deplacement(1610, 1263)
    # ----------
    minage(x_8, y_8)
    # ----------
    deplacement(520, 1231)
    deplacement(788, 1369)
    # ----------
    minage(x_7, y_7)
    # ----------
    deplacement(515, 1164)
    deplacement(141, 1345)
    # ----------
