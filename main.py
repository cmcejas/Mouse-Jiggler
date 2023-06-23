import pyautogui
import time

running = True

screenWidth, screenHeight = pyautogui.size()
x, y = pyautogui.position()

if(screenWidth - 1 == y and screenHeight - 1 == x):
  pyautogui.moveTo(x - 1, y - 1)
  time.sleep(45)
  pyautogui.moveTo(x, y)

else:
  pyautogui.moveTo(x + 1, y + 1)
  time.sleep(45)
  pyautogui.moveTo(x, y)
