import pyautogui
import time
import keyboard

while True:
    if keyboard.is_pressed('d'):
        print(pyautogui.position())
        time.sleep(1)
    elif keyboard.is_pressed('q'):
        print("Fin de la détection")
        break