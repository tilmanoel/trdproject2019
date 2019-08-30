import serial
import numpy as np
import requests
import time

#####
#Code to write data output from Arduino Uno into the
#InfluxDB database. Important values are data and params,
#which determine where/ the query is sent and what tags
#the read data is assigned. Note that as of now the code assumes only
#one voltage value from one source is being sent out. This will be
#extended to send all measured parameters from the Arduino to the database
#
#Author: Tilman Oelgeschlaeger
#Last edited: 30/08/2019
#####

params = (
   ('db','parameters'),
)
#note that data values should be edited for different measurements;
#the below is just as a test input

count = 0
type = '' #should eventually change depending on measurement
data = '' #appended depending on measurement parameter

ser = None
line = ''

def main():
	connected = False
	while True:
		try:
			ser = serial.Serial("/dev/ttyACM0",9600,timeout = 1)
			list = []
			for i in range(6):
				list.append(ser.readline()) #since this resets on each loop
#			print list
			connected = True

		except serial.SerialException:
			print "Device disconnected."
			connected = False
			if ser != None: #make ser null if nothing's at the serial port
				ser.close()
			time.sleep(1)

#		print ser.is_open,"connected = ",connected
		if connected:
#			print "In, line = ",line,":"
			for line in list:
  	   	 		if line != '':
					line.rstrip()
		       			terms = line.split(" ")
#					print terms[0]
       					if terms[0] == 'TV':
#	    					print 'in'
            					data = 'voltage,source=top value=' + terms[1]
	            			elif terms[0] == 'MV':
        	    				data = 'voltage,source=middle value=' + terms[1]
					elif terms[0] == 'BV':
       						data = 'voltage,source=bottom value=' + terms[1]
					elif terms[0] == 'TA':
						data = 'current,source=top value=' + terms[1]
					elif terms[0] == 'MA':
						data = 'current,source=middle value=' + terms[1]
					elif terms[0] == 'BA':
						data = 'current,source-bottom value=' + terms[1]
					else:
            					continue

#					print data
        				response = requests.post('http://localhost:8086/write',params=params,data=data)
#					print response.content
#   					print line,


main()
