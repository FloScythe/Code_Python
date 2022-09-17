import pyautogui
import keyboard
import time

while True:
    if keyboard.is_pressed('d'):
        print(pyautogui.position())
        time.sleep(1)
    elif keyboard.is_pressed('q'):
        print("Fin de la détection")
        break