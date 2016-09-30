#!/usr/bin/env python
"""

Creating a python function that returns coordinates of 
wherever the mouse is

"""
import pyautogui

def coordinates():
    return pyautogui.position()

def main():
    v= coordinates()
    print v

if __name__ == "__main__":
        main()

"""

$ ./mousecoordinates.py 
<class 'Xlib.protocol.request.QueryExtension'>
(256, 269)

$ ./mousecoordinates.py 
<class 'Xlib.protocol.request.QueryExtension'>
(541, 256)

"""
