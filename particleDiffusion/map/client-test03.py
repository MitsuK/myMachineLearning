import websocket
import thread
import time
import random

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
