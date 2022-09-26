import time
import keyboard
import pyautogui
import random
import unidecode
pyautogui.locateOnScreen("Ressource_Flo/Seigle.PNG", confidence=0.65)
print()
level = 54  # Niveau métier actuel
temps = 12 - (10 * level / 100)  # Temps de recolte
while True:
    action = False
    localisation = pyautogui.locateOnScreen("Ressource_Flo/Seigle.PNG", confidence=0.7)
    pyautogui.moveTo(localisation)
    if localisation:
        pyautogui.mouseDown()
        action = True

    non_disponible = pyautogui.locateOnScreen("Ressource_Flo/non_disponible.PNG", confidence=0.95)
    time.sleep(1)

    # ---- Cereale disponible ----
    if localisation and not non_disponible:
        print("Le céréale peut etre récupéré")
        pyautogui.click()
        action = True
        time.sleep(1)

    # ---- Cereale non disponible ----
    elif localisation and non_disponible:
        print("Le céréale est déjà pris")
        action = True

    if not action:
        time.sleep(temps)
        print("Il faut changer de carte")
        # ----- Controle des cartes de récolte -----
        map1 = pyautogui.locateOnScreen("Ressource_Flo/Map1.png")
        map2 = pyautogui.locateOnScreen("Ressource_Flo/Map2.png")
        if map1:
            print("Carte actuelle : 1")
            print("Changement de map")
            pyautogui.mouseUp()
            pyautogui.moveTo(1700, 1375, duration=random.uniform(0.2, 0.3))
            pyautogui.click()
            time.sleep(6)
        elif map2:
            print("Carte actuelle : 2")
            print("Changement de map")
            pyautogui.mouseUp()
            pyautogui.moveTo(1050, 55, duration=random.uniform(0.2, 0.3))
            pyautogui.click()
            time.sleep(6)

    pyautogui.mouseUp()