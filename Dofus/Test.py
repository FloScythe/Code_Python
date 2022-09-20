import pyautogui
import random
import time
import keyboard


# Trajet
go_out_0 = [979, 677]
go_out_1 = [493, 905]
go_out_2 = [686, 730]  # Map vide

go_back_2 = [1635, 999]
go_back_1 = [1499, 1132]  # Map vide
go_back_0 = [1511, 1073]


def mouvement(x,y):
    pyautogui.moveTo(x,y, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(6)

mouvement(go_out_0[0],go_out_0[1])