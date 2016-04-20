import os
import sys
import threading
from socket import socket, AF_INET, SOCK_STREAM

from flask import Flask, request #, jsonity

app = Flask(__name__)


stdoutmutex = threading.Lock()
mapPort = 50008
#providerPort = 50009
host = 'localhost'

@app.route('/', methods=['GET'])
def hello():
    return "hello"


if __name__ == "__main__":

    #sock = socket(AF_INET, SOCK_STREAM)
    #sock.bind((host, mapPort))
    #sock.listen(5)


    #host = 'localhost'
    #port = 50009
    #httpd = BaseHTTPServer((host, providerPort), MyHandler)
    #print('serving at port', providerPort)
    #httpd.serve_forever()
    #sockProvider = socket(AF_INET, SOCK_STREAM)
    #sockProvider.bind((host, providerPort))
    #sockProvider.listen(5)
    
    #app.run(debug=True, port=providerPort)
    app.run(debug=True, port=mapPort)


    while True:
        conn, addr = sock.accept()
        data = conn.recv(1024)
        with stdoutmutex:
            print data
            reply = 'server got : [%s]\n' % data
            conn.send(reply.encode())

        #connProvider, addrProvider = soclProvider.accept()
        #connProvider.send("aaaaaaa".encode())

