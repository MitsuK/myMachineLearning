from time import sleep
import paho.mqtt.client as mqtt

host="test.mosquitto.org"
port = 1883
topic = "mitsu/gold/egg"

client = mqtt.Client(protocol=mqtt.MQTTv31)

client.connect(host, port=port, keepalive=60)

for i in range(3):
    client.publish(topic, 'ham')
    sleep(0.2)

client.disconnect()
