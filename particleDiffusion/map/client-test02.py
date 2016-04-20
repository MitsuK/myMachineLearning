from time import sleep
import os
import sys
import threading
from socket import socket, AF_INET, SOCK_STREAM

import random

_updateUrl = "/updateVehicleStatus"
vehicleId = 1
stdoutmutex = threading.Lock()
port = 5000
host = 'localhost'


def sendStatus(text):
    ###################
    '''
    Socket program to
     sending text to map server.
    '''
    ###################

    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((host, port))
        ##sock.send(name.encode())
        httpReqText = "GET " + _updateUrl + "?vehicleId=001" + " HTTP/1.1\r\n\r\n"
        #sock.send(text.encode())
        sock.send(httpReqText)
        reply = sock.recv(0)
        sock.close()
        with stdoutmutex:
            print 'client got : [%s]' % reply
    except Exception, msg:
        with stdoutmutex:
            print'failed to send status' 

def updateStatus(pos):
    if random.randint(0,1) == 0:
        pos[0] += 1
    else:
        pos[1] += 1
    
if __name__ == "__main__":
    pos = [0,0]

    while True:
        json = "{ 'position': " + str(pos) + "}"
        with stdoutmutex:
            print json
        sendStatus(json)
        sleep(1)
        updateStatus(pos)

