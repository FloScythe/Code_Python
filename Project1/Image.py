import pyautogui
import keyboard
import time

# from python_imagesearch.imagesearch import imagesearch
# pos1 = imagesearch("Pos1.png",precision=0.5)
# if pos1[0] != -1:
#     print("Personnage position : ", pos1[0], pos1[1])
# else:
#     print("image not found")

z = pyautogui.locateOnScreen("Pos1.png",confidence = 0.8)
pyautogui.moveTo(z)