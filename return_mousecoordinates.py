#!/usr/bin/env python
"""

Creating a python function that moves mouse to assigned
coordinates(x,y) and makes it stay for certain time 't' (in sec).
e.g. move_to_coordinates(x,y,t)

P.S. Do noy touch you mouse or laptop's touch pad when
executing this file

"""
import pyautogui,sys

def move_to_coordinates(x,y):
    return  pyautogui.moveTo(x,y)
    
def main():
    mv_coordinates= move_to_coordinates(100,200)
    print mv_coordinates


if __name__ == "__main__":
    main()

    
