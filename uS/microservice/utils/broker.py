import paho.mqtt.client as mqtt
import time

mqttBroker ="mqtt.eclipseprojects.io" 

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker) 

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)
    
    
def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Smartphone")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe("TEMPERATURE")
client.on_message=on_message 

time.sleep(30)
client.loop_stop()