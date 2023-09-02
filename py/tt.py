import paho.mqtt.publish as publish

publish.single("ifn649","LED_OFF",hostname="13.239.37.158")
print("Done, LED is OFF")
