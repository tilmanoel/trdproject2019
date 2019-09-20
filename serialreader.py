#!/usr/bin/env python
import sys

#print(sys.path)

import serial
import numpy as np
import math
import requests
import time

#####
#Code to write data output from an Arduino Uno into an
#InfluxDB database. Important values are data and params,
#which determine where/how the query is sent and what tags
#the read data is assigned. The code on the Arduino is given 
#on the Github page.
#Author: Tilman Oelgeschlaeger
#Last edited: 19/09/2019
#####

params = (
   ('db','parameters'),
)

proxies = {

	"http": None,
	"https": None,

}

#note that data values should be edited for different measurements;

def main():
	ser = None
	connected = False
	while True:
		try:
			print "Connecting... ",
			ser = serial.Serial("/dev/ttyACM0",9600,timeout = 1) #connect to serial port (must be done every time to ensure reconnection when
			print "Finished connecting"			     #Arduino disconnects
			list = []
			while(len(list) < 6):
#				print "Reading"
				line = ser.readline(12).rstrip() #read serialport
				if line != '':
#					print line
					list.append(line)
#					print list[len(list) -1]
#				print "Done"

			connected = True


		except serial.SerialException as e:
			print "Device disconnected (SerialException).",str(e)
			connected = False
			if ser != None: #make ser null if nothing's at the serial port
				ser.close()
			time.sleep(1)


		except OSError as e:
			print "Device disconnected (OS Error).",str(e)
			connected = False
			if ser != None:
				ser.close()
			time.sleep(1)

#		print ser.is_open,"connected = ",connected
		if connected:
#			print "In, line = ",line,":"
			for line in list:
		       		terms = line.split(" ")
#				print terms[0]
				if len(terms) == 3 and ((terms[2] == 'A' or terms[2] == 'V')): #serial port sometimes outputs values wrong
					val = 5.0*float(terms[1])/1023.0		       #this if is to ensure program continues
#					print val*1023.0/5.0				       #running
					if terms[0] == 'TV':
						val *= 4.1/1.00684261975		       #calculated from digital display
						data = 'voltage,source=top value=' + str(val)
					elif terms[0] == 'MV':
						val *= 2.2/0.57673509286
#						print val
						data = 'voltage,source=middle value=' + str(val)
					elif terms[0] == 'BV':
						val *=2.2/0.557184750733
#						print val
						data = 'voltage,source=bottom value=' + str(val)
					elif terms[0] == 'TA':
						val *= 10.1/2.13098729238
						data = 'current,source=top value=' + str(val)
					elif terms[0] == 'MA':
						val *= 5.5/1.12903225806
						data = 'current,source=middle value=' + str(val)
					elif terms[0] == 'BA':
						val *= 1.6/0.283479960899
						data = 'current,source=bottom value=' + str(val)
					else:
            					continue

#					print "final line:", line
#					print data
					try:
						response = requests.post('http://localhost:8086/write',params=params,data=data,proxies=proxies)

					except requests.exceptions.ProxyError as e:
						print ("Unable to send HTTP request.")
#					print response.content

			ser.close() #close port

main()
