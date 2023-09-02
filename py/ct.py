import paho.mqtt.client as mqtt
import serial



def on_connect(client, userdata, flags, rc): # func for making connection
	print(f"Connected to MQTT Server {ADD} at port {PORT}")
	print("Connection returned result: " +str(rc))
	topic = "hey7"
	client.subscribe("hey7")
	print(f"Subscribed to topic: {topic} ")

def on_message(client, userdata, msg): 	#Func For Sending msg
	print(msg.topic+" "+str(msg.payload))
	print("relaying to teensy over BT...")
	
	ser = serial.Serial("/dev/rfcomm0", 9600)
	ser.write(msg.payload)
	
ADD = "13.210.48.244"
PORT = 1883
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(ADD, PORT, 60)

client.loop_forever()
