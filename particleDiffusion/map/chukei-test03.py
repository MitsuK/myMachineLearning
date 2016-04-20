import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import websocket
import thread
import time
import random

import json

_vehicleNameArray = []
_vehiclePropertyArray = []

'''
class MainHandler(tornado.web.RequestHandler):
#class MainHandler(tornado.websocket.WebSocketHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
    def get(self):
        #return json.dumps(_vehiclePropertyArray)
        self.write(json.dumps(_vehiclePropertyArray))
        #loader = tornado.template.Loader(".")
        #self.write(loader.load("index.html").generate())

class WS2Handler(tornado.websocket.WebSocketHandler):
    @tornado.web.asynchronous
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")

    def open(self):
        print 'connection opened...'
        self.write_message("The server says: 'Hello'. Connection was accepted.")
        #self.write_message("The server says: 'Hello'. Connection was accepted.")

    def on_message(self, message):
        #self.write_message("The server says: " + message + " back at you")
        #print 'received:', message
        self.write_message(json.dumps(_vehiclePropertyArray))

    def on_close(self):
        print 'connection closed...'



class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'connection opened...'
        #self.write_message("The server says: 'Hello'. Connection was accepted.")

    def on_message(self, message):
        #self.write_message("The server says: " + message + " back at you")
        print 'received:', message
        self.checkVehicleExist(message)

    def on_close(self):
        print 'connection closed...'


    def checkVehicleExist(self, msg):
        #print msg
        _tmp = json.loads(msg)
        if _tmp["vehicleId"] in _vehicleNameArray:
            self.updateMapStatus(_tmp)
        else:
            self.addNewVehicle(_tmp)

    def addNewVehicle(self, vehicleStatus):
        _vehicleNameArray.append( vehicleStatus["vehicleId"] )
        _vehiclePropertyArray.append(vehicleStatus)

    def updateMapStatus(self, vehicleStatus):
        #print msg
        _vehiclePropertyArray[_vehicleNameArray.index(vehicleStatus["vehicleId"])] = vehicleStatus


application = tornado.web.Application([
    (r'/cur', WS2Handler),
    (r'/ws', WSHandler),
    (r'/get', MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])

if __name__ == "__main__":
    application.listen(9091)
    tornado.ioloop.IOLoop.instance().start()
'''
    

_vehicleId = 002
_pos = [0,0]

def on_message(ws, message):
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    def run(*args):
        for i in range(10):
            updateVehicleStatus()
            time.sleep(1)
            jsonText = '{ "vehicleId": ' + str(_vehicleId) + ', "pos": ' + str(_pos) + ' }'
            #ws.send("Hello %d" % i)
            ws.send(jsonText)
        time.sleep(1)
        ws.close()
        print "thread terminating..."
    thread.start_new_thread(run, ())

def updateVehicleStatus():
    _pos[random.randint(0,1)] += random.randint(0, 2) - 1


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:9090/ws",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
