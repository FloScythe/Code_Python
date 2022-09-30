import random
import time
import keyboard
import pyautogui


def clics(x, confidence):
    position = pyautogui.locateOnScreen(x, confidence=confidence)
    pyautogui.moveTo(position, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(0.5)


def fenetre():
    # Fenetre
    while pyautogui.locateOnScreen("Métier/Ressource_Flo/Quit.png", confidence=0.8):
        clics("Métier/Ressource_Flo/Quit.png", 0.8)


def combat(x, y):
    # Combat
    if pyautogui.locateOnScreen("Combat/Pret.png", grayscale=True, confidence=0.8) or pyautogui.locateOnScreen(
            "Combat/Findetour.png", grayscale=True, confidence=0.8):
        clics("Combat/Pret.png", 0.8)

        print("Debut du mode combat")
        # Boucle infini :
        while True:
            match = pyautogui.pixelMatchesColor(x, y, (73, 97, 37))
            if match:
                while match:
                    clics("Combat/invoc_tofu.png", 0.8)
                    clics("Combat/invoc2.png", 0.8)
                    pyautogui.click()
                    match = pyautogui.pixelMatchesColor(x, y, (73, 97, 37))

                clics("Combat/Findetour.png", 0.8)
                time.sleep(3)

            elif not match:
                pyautogui.moveTo(pyautogui.locateOnScreen("Combat/Deplacement.png", confidence=0.8),
                                 duration=random.uniform(0.1, 0.3))
                pyautogui.doubleClick(duration=0.5)
                clics("Combat/Findetour.png", 0.8)
                pyautogui.click()
                time.sleep(3)

            resume = pyautogui.locateOnScreen("Combat/Quit.png", confidence=0.8)
            dead = pyautogui.locateOnScreen("Combat/dead.png")
            if resume and not dead:
                print("C'est gagné!")
                print("Fin du mode combat")
                clics("Combat/Quit.png", 0.8)
                return
            else:
                print("Tu as perdu!")
                print("Fin du mode combat")
                clics("Combat/Quit.png", 0.8)

    else:
        print("Pas de combat détecté")


def Piou():
    while True:
        a = pyautogui.locateOnScreen("Combat/Piou.png", grayscale=True, confidence=0.8)
        b = pyautogui.locateOnScreen("Combat/Piou1.png", grayscale=True, confidence=0.8)
        c = pyautogui.locateOnScreen("Combat/Piou2.png", grayscale=True, confidence=0.8)
        d = pyautogui.locateOnScreen("Combat/Piou3.png", grayscale=True, confidence=0.8)

        if a:
            z = a
            pyautogui.moveTo(z, duration=random.uniform(0.1, 0.2))
            pyautogui.click()
            time.sleep(0.5)
            if pyautogui.locateOnScreen("Combat/Attaquer.png", confidence=0.8):
                print("Attaque")
                attack = pyautogui.locateOnScreen("Combat/Attaquer.png", confidence=0.8)
                pyautogui.moveTo(attack, duration=random.uniform(0.1, 0.3))
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(5)
                break
        elif b:
            z = b
            pyautogui.moveTo(z, duration=random.uniform(0.1, 0.2))
            pyautogui.click()
            time.sleep(0.5)
            if pyautogui.locateOnScreen("Combat/Attaquer.png", confidence=0.8):
                print("Attaque")
                attack = pyautogui.locateOnScreen("Combat/Attaquer.png", confidence=0.8)
                pyautogui.moveTo(attack, duration=random.uniform(0.1, 0.3))
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(5)
                break
        elif c:
            z = c
            pyautogui.moveTo(z, duration=random.uniform(0.1, 0.2))
            pyautogui.click()
            time.sleep(0.5)
            if pyautogui.locateOnScreen("Combat/Attaquer.png", confidence=0.8):
                print("Attaque")
                attack = pyautogui.locateOnScreen("Combat/Attaquer.png", confidence=0.8)
                pyautogui.moveTo(attack, duration=random.uniform(0.1, 0.3))
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(5)
                break
        elif d:
            z = d
            pyautogui.moveTo(z, duration=random.uniform(0.1, 0.2))
            pyautogui.click()
            time.sleep(0.5)
            if pyautogui.locateOnScreen("Combat/Attaquer.png", confidence=0.8):
                print("Attaque")
                attack = pyautogui.locateOnScreen("Combat/Attaquer.png", confidence=0.8)
                pyautogui.moveTo(attack, duration=random.uniform(0.1, 0.3))
                time.sleep(0.1)
                pyautogui.click()
                time.sleep(5)
                break
        combat(2108, 415)


while not keyboard.is_pressed("q"):
    Piou()
    if pyautogui.locateOnScreen("Ressource/Repos.png"):
        assis = pyautogui.locateOnScreen("Combat/assis.png", confidence=0.8)
        pyautogui.moveTo(assis, duration=random.uniform(0.1, 0.3))
        pyautogui.doubleClick()
        time.sleep(30)
