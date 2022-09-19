import pyautogui
import keyboard
import time

pyautogui.moveTo(1792,431)
pyautogui.click()

z1 = pyautogui.locateOnScreen("Pos1.png",grayscale=False,confidence = 0.5)
pyautogui.moveTo(z1)
z2 = pyautogui.locateOnScreen("Pos2.png",grayscale=False,confidence = 0.5)
pyautogui.moveTo(z2)
z3 = pyautogui.locateOnScreen("Pos3.png",grayscale=False,confidence = 0.5)
pyautogui.moveTo(z3)
z4 = pyautogui.locateOnScreen("Pos4.png",grayscale=False,confidence = 0.5)
pyautogui.moveTo(z4)

z5 = pyautogui.locateOnScreen("invoc2.png",confidence = 0.8)
pyautogui.moveTo(z5)
pyautogui.click()
pyautogui.click()

z6 = pyautogui.locateOnScreen("Findetour.png",confidence = 0.8)
pyautogui.moveTo(z6)
pyautogui.click()