import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template

import json

_vehicleNameArray = []
_vehiclePropertyArray = []

class MainHandler(tornado.web.RequestHandler):
#class MainHandler(tornado.websocket.WebSocketHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
    def get(self):
        #return json.dumps(_vehiclePropertyArray)
        #self.write(json.dumps(_vehiclePropertyArray))
        loader = tornado.template.Loader(".")
        self.write(loader.load("index.html").generate())

class WS2Handler(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True
    def open(self):
        print 'connection opened...'
        #self.write_message("The server says: 'Hello'. Connection was accepted.")
        #self.write_message("connected: WS2Handler")
        #self.write_message("The server says: 'Hello'. Connection was accepted.")

    def on_message(self, message):
        #self.write_message("The server says: " + message + " back at you")
        print 'received:', message
        print _vehiclePropertyArray
        self.write_message(json.dumps(_vehiclePropertyArray))

    def on_close(self):
        print 'connection closed...'



class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print 'connection opened...'
        self.write_message("The server says: 'Hello'. Connection was accepted.")

    def on_message(self, message):
        #self.write_message("The server says: " + message + " back at you")
        #  mawari no jokyo kaesu
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
    (r'/', MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])

if __name__ == "__main__":
    application.listen(9090)
    tornado.ioloop.IOLoop.instance().start()