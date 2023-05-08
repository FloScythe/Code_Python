import pyautogui
import time

while True:
    x, y = pyautogui.position()
    position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    print(position_str, end='')
    print(" -- ")
    print('\b' * len(position_str), end='', flush=True)
    time.sleep(1)

