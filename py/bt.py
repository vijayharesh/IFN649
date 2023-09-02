#!/usr/bin/env python3
import serial
import time
import string

# Reading and writing data from and to Arduino serially.
# rfcomm0 -> this could be different
ser = serial.Serial("/dev/rfcomm0", 9600)
ser.write(str.encode('Start\r\n'))

while True:
    if ser.in_waiting > 0:
        raw_serial = ser.readline()
        cooked_serial = raw_serial.decode('utf-8').strip('\r\n')
        print(cooked_serial)
