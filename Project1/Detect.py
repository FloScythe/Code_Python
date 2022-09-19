import pyautogui
import time
from pynput import keyboard


def on_press(key):
    try:
        print(key.char)
    except AttributeError:
        print("Fin de la boucle")
        return False


while True:

    # with keyboard.Listener(on_press=on_press) as listener :

        if listener == 'd':
            print(pyautogui.position())
            time.sleep(1)
        elif listener == 'q':
            print("Fin de la détection")
            break

# Collect events until released
