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
    s.bind((host, port))        
    s.listen(5)                 
    x,y = pyautogui.position()
    positionStr = "The coordinates of Mouse are("+str(x).rjust(4)+',' + str(y).rjust(4) + ")"
    while True:
        c, addr = s.accept()    
        print 'Got connection from', addr
        c.send(positionStr)
        c.close()                # Close the connection


def main():
    VShareITServerSocketToSendMouseCoordiantes()

if __name__ == "__main__":
    main()
"""
$ python mice_server_sending_coordinates_to_client.py &
samad:~/VShareIT$ <class 'Xlib.protocol.request.QueryExtension'>
samad:~/VShareIT$ python mice_client.py 
Got connection from ('127.0.0.1', 48230)
The coordinates of Mouse are( 982, 354)

"""

