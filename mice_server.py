#!/usr/bin/python         

#This program is written for a product named VShareIT. Feel free to use 
#this code for other projects. We dont't take responsibility for further 
#use of this code for any other project. 

#File Name: mice_server.py 
#Discription: Server Code for the Mice Control
#Written by: 
#Zain Ijaz (Inventor and Developer)
#Abdul Samad ( Lead Developer )

import socket               
import sys


def VShareITServerSocketInit():
    """Function Initializes the Eth Socket for Communication between the Server & Client"""
    s = socket.socket()         
    host = socket.gethostname() 
    port = 12345                
    s.bind((host, port))        
    s.listen(5)                 
    while True:
        c, addr = s.accept()    
        print 'Got connection from', addr
        c.send('Thank you for connecting')
        c.close()                # Close the connection


def main():
    VShareITServerSocketInit()


if __name__ == "__main__":
    main()
