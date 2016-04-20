from flask import Flask, request
#from signal import signal, SIGPIPE, SIG_DFL
#signal(SIGPIPE,SIG_DFL) 



app = Flask(__name__)

@app.route("/", methods=["GET"])
def getMapStatus():
    return "{data:[1,2,3]}"

@app.route("/updateVehicleStatus", methods=["GET"])
def updateCarStatus():
    print request.args.get("vehicleId")
    return ""

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
