import pyautogui
import random
import time

# Chemin jusqu'a la mine
for i in range(2):
    pyautogui.moveTo(1013, 1169, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(4)
for y in range(8):
    pyautogui.moveTo(251, 626, duration=random.uniform(0.1, 0.3))
    pyautogui.click()
    time.sleep(6)
