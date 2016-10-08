#!/usr/bin/python         

#This program is written for a product named VShareIT. Feel free to use 
#this code for other projects. We dont't take responsibility for further 
#use of this code for any other project. 

#File Name: mice_server_sending_coordinates_to_client.py 
#Discription: Server Code for sending the Mouse's Coordinates to
#client
#Written by: 
#Zain Ijaz (Inventor and Developer)
#Abdul Samad ( Lead Developer )



import socket               
import sys
import pyautogui

print('Press Ctrl-C to quit.')

def VShareITServerSocketToSendMouseCoordiantes():
    """Function Initializes the Eth Socket for Communication between the Server & Client"""
    s = socket.socket()         
    host = socket.gethostname() 
    port = 12345                
    s.bind(("192.168.56.101", port))        
    s.listen(5)                 
    c, addr = s.accept()    
    print 'Got connection from', addr
    while True:
       x,y = pyautogui.position()
       positionStr = str(x).rjust(4)+',' + str(y).rjust(4) 
       c.send(positionStr)

def main():
    VShareITServerSocketToSendMouseCoordiantes()

if __name__ == "__main__":
    main()
"""

$ ./mice_server.py 
<class 'Xlib.protocol.request.QueryExtension'>
Press Ctrl-C to quit.
Got connection from ('192.168.56.102', 46658)

$./mice_client.py
659, 536
659, 536
659, 536
659, 536
659, 536
659, 536 659, 536 659, 536 659, 536 659, 536 659, 536 659, 536 659, 536 659, 536
659, 536
.
.
.
.
P.S and it goes on unless Ctrl+c is pressed
"""
