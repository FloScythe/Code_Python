import pyautogui
import keyboard
import time

# from python_imagesearch.imagesearch import imagesearch
# pos = imagesearch("Test.png",precision=0.8)
# if pos[0] != -1:
#     print("position : ", pos[0], pos[1])
#     pyautogui.moveTo(pos[0],pos[1])
# else:
#     print("image not found")

while True:
    if keyboard.is_pressed('d'):
        print(pyautogui.position())
        time.sleep(1)
    elif keyboard.is_pressed('q'):
        print("Fin de la détection")
        break
