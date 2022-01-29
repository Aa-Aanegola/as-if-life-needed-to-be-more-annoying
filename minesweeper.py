#!/usr/bin/env python3

import random
import webbrowser
import screen_brightness_control as sbc
import time
from pynput import keyboard
import os
from string import ascii_lowercase

SIUUU = 'https://www.youtube.com/watch?v=ocnUuhajSFc'
alphaSet = []
alphaUnset = []

def on_press(key):
    try:
        if key.char in alphaSet:
            SPAMM()
            time.sleep(2)
    except AttributeError:
        if(key._name_ == 'space'):
            updateSet()
        pass


def SPAMM():
    for i in range(10):
        webbrowser.open_new(SIUUU)
        if i % 2 == 0:
            sbc.fade_brightness(1,start=100,interval=0.01,increment=5)
        else:
            sbc.fade_brightness(100,start=1,interval=0.01,increment=5)
        time.sleep(0.5)

def updateSet(): 
    probability = input("Enter probability of letter to be a mine: ")
    alphaSet.clear()
    alphaUnset.clear()
    for c in ascii_lowercase:
        choice = random.randint(1,100)
        if choice <= int(probability):
            alphaSet.append(c)
        else:
            alphaUnset.append(c)
    print("Mines Set :)")


updateSet()

with keyboard.Listener(
    on_press = on_press
    ) as listener:
        listener.join()