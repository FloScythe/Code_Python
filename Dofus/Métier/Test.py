import random
import time

import pyautogui


def souris(nom):
    z = pyautogui.locateOnScreen(nom, confidence=0.8)
    pyautogui.moveTo(z, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(0.5)


def sell(x):
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


# if not pyautogui.locateOnScreen("Ressource_Flo/Full.png", confidence=0.8):
#     sell("Ressource_Flo/Ble_inventaire.png")
#     sell("Ressource_Flo/Orge_inventaire.png")
#     sell("Ressource_Flo/Avoine_inventaire.png")
# else:
#     print("Rien a vendre")
#     souris("../Combat/Quit.png")

souris("../Ressource/Inventaire.png")
souris("Ressource_Flo/Alerte_full.PNG")
full = pyautogui.locateOnScreen("Ressource_Flo/Alerte_full.PNG", confidence=0.8)
if full:
    print("Trouvé")
    while full:
        # sell("Ressource_Flo/Ble_inventaire.png")
        # sell("Ressource_Flo/Orge_inventaire.png")
        # sell("Ressource_Flo/Avoine_inventaire.png")
        sell("Ressource_Flo/Houblon_inventaire.png")
        souris("../Ressource/Inventaire.png")
        full = pyautogui.locateOnScreen("Ressource_Flo/Alerte_full.PNG", confidence=0.8)
        if not full:
            souris("../Combat/Quit.png")
