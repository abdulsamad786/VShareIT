#!/usr/bin/python         

#This program is written for a product named VShareIT. Feel free to use 
#this code for other projects. We dont't take responsibility for further 
#use of this code for any other project. 

#File Name: mice_client.py 
#Discription: Client Code for the Mice Control
#Written by: 
#Zain Ijaz (Inventor and Developer)
#Abdul Samad ( Lead Developer )

import socket               

def VShareITClientSocketInit():
    s = socket.socket()         
    host = socket.gethostname()
    port = 12345                
    s.connect(("192.168.56.101", port))
    while True:
        print s.recv(1024)
    s.close                     

def main():
    VShareITClientSocketInit()

if __name__ == "__main__":
    main()

