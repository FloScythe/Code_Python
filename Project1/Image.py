import pyautogui
import keyboard
import time

from python_imagesearch.imagesearch import imagesearch
pos1 = imagesearch("Pos1.png",precision=0.5)
pyautogui.locateOnScreen("Pos1.png",confidence = 0.5)
pos5 = imagesearch("Combat2.png",precision=0.8)
pos2 = imagesearch("Pos2.png",precision=0.5)
pos3 = imagesearch("Pos3.png",precision=0.5)
pos4 = imagesearch("Pos4.png",precision=0.5)

if pos1[0] != -1:
    print("Personnage position : ", pos1[0], pos1[1])
elif pos2[0] != -1:
    print("Personnage position : ", pos2[0], pos2[1])
elif pos3[0] != -1:
    print("Personnage position : ", pos3[0], pos3[1])
elif pos4[0] != -1:
    print("Personnage position : ", pos4[0], pos4[1])
else:
    print("image not found")

if pos5[0] != -1:
    print("Combat : ", pos1[0], pos1[1])