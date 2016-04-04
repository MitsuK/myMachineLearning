import paho.mqtt.client as mqtt

host="test.mosquitto.org"
port=1883
topic="mitsu/gold/egg"

def on_connect(client, userdata, flags, response_code):
    print('status {0}'.format(response_code))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))

if __name__ == '__main__':

    client = mqtt.Client(protocol=mqtt.MQTTv31)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host, port=port, keepalive=60)

    client.loop_forever()
    
