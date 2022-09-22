import pyautogui
import time
import keyboard

# while 1:

while True:
    if keyboard.is_pressed('d'):
        x, y = pyautogui.position()
        r, g, b = pyautogui.pixel(x, y)
        print(pyautogui.position(), r, g, b)
        x, y = pyautogui.position()
        r,g,b = pyautogui.pixel(x, y)
        print(pyautogui.position(),r,g,b)
        time.sleep(1)
    elif keyboard.is_pressed('q'):
        print("Fin de la détection")
        break
