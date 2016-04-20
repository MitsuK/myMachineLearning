import sys
import websocket
import thread
import time
import random


_vehicleId = 001
_pos = [0,0]

def on_message(ws, message):
    print message

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    def run(*args):
        for i in range(30):
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
    _pos[0] += random.randint(0, 5) - 3
    _pos[1] += random.randint(0, 5) - 3
    print _pos


if __name__ == "__main__":
    if (len(sys.argv) > 1):
        _vehicleId = int(sys.argv[1])
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:9090/ws",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
