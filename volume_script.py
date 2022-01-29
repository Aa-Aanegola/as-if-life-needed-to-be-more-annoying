import os
os.system('xhost +')
import pyautogui
import keyboard
import time
import math
import alsaaudio

globalPosition = (0,0)
maxPosition = (1920,1080)
mixer = alsaaudio.Mixer()

while True:
    if keyboard.is_pressed('s'):
        print("Updated global position")
        globalPosition = pyautogui.position()
    elif keyboard.is_pressed('u'):
        print("Unset global position")
        globalPosition = (0,0)
    elif keyboard.is_pressed('q'):
        break
    curPosition = pyautogui.position()
    xVal = abs(curPosition[0] - globalPosition[0])/maxPosition[0]
    yVal = abs(curPosition[1] - globalPosition[1])/maxPosition[1]
    volume = math.sqrt(xVal**2 + yVal**2) * 100
    print(volume)
    if volume > 100:
        volume = 100
    mixer.setvolume(int(volume))
    
