import paho.mqtt.publish as publish
publish.single("hey7", "Hello World", hostname="13.210.48.244")
print("Done")
