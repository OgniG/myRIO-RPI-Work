#!/usr/bin/env python
import time
import serial
i=0
#setting up infinite loop
while i>-1:
	ser1 = serial.Serial(
	#HR monitor serial port referred
			port='/dev/rfcomm0',
			baudrate = 9600,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS,
			timeout=1
		 )
	counter=0
	x = []
	data = []
	x=ser1.read(60),
	#reads first 120 bytes	
	data.append(x),
	#adds data to the list
	ser = serial.Serial(
		#refers to USB serial output to myRIO
		port='/dev/ttyAMA0',
		baudrate = 9600,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS,
		timeout=1
		)
	counter=0
	for f in data:
		data1 = str(data)
	#converts data to string
	data2=data1.encode("hex"),
	#converts data to hexadecimal tuple
	for f in data2:
		data3= str(data2)
	#converts tuple to string again
	ser.write (data3),
	#writes data to serial port
	print data3
	#empties list for next round
	data = [];
	i += 1
