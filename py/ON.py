import paho.mqtt.publish as publish

publish.single("hey7","LED_ON",hostname="13.210.48.244")
print("Done, LED is ON.")
