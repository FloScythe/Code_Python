import pyautogui
import random
import time
import keyboard


def combat():
    if pyautogui.locateOnScreen("Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "Combat/Findetour.png", grayscale=True, confidence=0.8):

        p = pyautogui.locateOnScreen("Combat/Pret.png", confidence=0.8)
        pyautogui.moveTo(p, duration=random.uniform(0.1, 0.3))
        pyautogui.click()

        while True:
            z = pyautogui.locateOnScreen("Combat/invoc1.png", confidence=0.8)
            pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
            pyautogui.click()

            time.sleep(random.uniform(0.1, 0.2))

            z1 = pyautogui.locateOnScreen("Combat/Pos1.png", grayscale=False, confidence=0.6)
            pyautogui.moveTo(z1)
            z2 = pyautogui.locateOnScreen("Combat/Pos2.png", grayscale=False, confidence=0.6)
            pyautogui.moveTo(z2)
            z3 = pyautogui.locateOnScreen("Combat/Pos3.png", grayscale=False, confidence=0.6)
            pyautogui.moveTo(z3)
            z4 = pyautogui.locateOnScreen("Combat/Pos4.png", grayscale=False, confidence=0.6)
            pyautogui.moveTo(z4)

            time.sleep(random.uniform(0.1, 0.2))

            z5 = pyautogui.locateOnScreen("Combat/invoc2.png", confidence=0.8)
            pyautogui.moveTo(z5, duration=random.uniform(0.1, 0.3))
            pyautogui.click()
            pyautogui.click()
            time.sleep(0.5)

            if pyautogui.pixelMatchesColor(1794, 429, (36, 48, 18)):
                z6 = pyautogui.locateOnScreen("Combat/Findetour.png", confidence=0.8)
                pyautogui.moveTo(z6, duration=random.uniform(0.1, 0.3))
                pyautogui.click()
                time.sleep(1)

            if pyautogui.locateOnScreen("Combat/Quit.png", confidence=0.8):
                z7 = pyautogui.locateOnScreen("Combat/Quit.png", confidence=0.8)
                pyautogui.moveTo(z7, duration=random.uniform(0.1, 0.3))
                pyautogui.click()
                break
            elif keyboard.is_pressed("q"):
                break


def level_up():
    # Detection en cas de level up
    level_up = pyautogui.locateOnScreen("level_up.png", confidence=0.8)
    pyautogui.moveTo(level_up, duration=random.uniform(0.1, 0.3))
    pyautogui.click()


# Map 1
liste_x_1 = [895, 1100, 1161, 1563, 1616]
liste_y_1 = [726, 430, 457, 637, 665]
ressource_1 = len(liste_x_1)
repos1 = ressource_1*random.uniform(12,12.5)
# Map 2
liste_x_2 = [1527, 1475, 1433, 1167, 1002, 941, 802, 743, 481, 442]
liste_y_2 = [746, 724, 703, 562, 496, 527, 586, 619, 738, 758]
ressource_2 = len(liste_x_2)
repos2 = ressource_2*random.uniform(12,12.5)
# Map 3
liste_x_3 = [1356, 1305, 1265, 1138, 1083, 501, 434]
liste_y_3 = [589, 568, 554, 526, 562, 645, 677]
ressource_3 = len(liste_x_3)
repos3 = ressource_3*random.uniform(12,12.5)

# Trajet
go_out_0 = [923, 626]
go_out_1 = [563, 800]
go_out_2 = [710, 668]  # Map vide

go_back_2 = [1444, 878]
go_back_1 = [1317, 971]  # Map vide
go_back_0 = [1317, 971]


while keyboard.is_pressed('q') == True:
    time.sleep(5)
    # Map 1
    for i in range(ressource_1):
        pyautogui.moveTo(liste_x_1[i], liste_y_1[i], duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        time.sleep(random.uniform(0.1, 0.3))
        level_up()
        combat()
    time.sleep(repos1)

    pyautogui.moveTo(go_out_0[0], go_out_0[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(5)

    if keyboard.is_pressed('q'):
        print("Interruption de la boucle")
        break

    # Map 2
    for i in range(ressource_2):
        pyautogui.moveTo(liste_x_2[i], liste_y_2[i], duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        time.sleep(random.uniform(0.1, 0.3))
        level_up()
        Combat
    time.sleep(repos2)
    pyautogui.moveTo(go_out_1[0], go_out_1[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(5)

    #Entree map vide
    pyautogui.moveTo(go_out_2[0], go_out_2[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(6)
    #Sorti map vide

    if keyboard.is_pressed('q'):
        print("Interruption de la boucle")
        break

    #Map 3
    for i in range(ressource_3):
        pyautogui.moveTo(liste_x_3[i], liste_y_3[i], duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        time.sleep(random.uniform(0.1, 0.3))
        level_up()
        Combat
    time.sleep(repos3)

    pyautogui.moveTo(go_back_2[0], go_back_2[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(go_back_1[0], go_back_1[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(5)

    # Map 2
    for i in range(ressource_2):
        pyautogui.moveTo(liste_x_2[i], liste_y_2[i], duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        time.sleep(random.uniform(0.1, 0.3))
        level_up()
        Combat
    time.sleep(repos2)

    pyautogui.moveTo(go_back_1[0], go_back_1[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(5)

    # Map 1
    for i in range(ressource_1):
        pyautogui.moveTo(liste_x_2[i], liste_y_2[i], duration=random.uniform(0.1, 0.3))
        pyautogui.click()
        time.sleep(random.uniform(0.1, 0.3))
        level_up()
        Combat
    time.sleep(repos1)

    pyautogui.moveTo(go_back_0[0], go_back_0[1], duration=random.uniform(0.1, 0.3))
    pyautogui.click()