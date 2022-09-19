import pyautogui
import keyboard
import time

z = pyautogui.locateOnScreen("Pos1.png",confidence = 0.5)
pyautogui.moveTo(z)