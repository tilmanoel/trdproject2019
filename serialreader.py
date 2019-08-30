import serial
import numpy as np
import requests
import time

#####
#Code to write data output from an Arduino Uno into an
#InfluxDB database. Important values are data and params,
#which determine where/how the query is sent and what tags
#the read data is assigned. Currently the code reads only low voltage
#values, reading of the sensors on the Arduino weather shield has
#not yet been implemented. The code on the Arduino is given on the Github
#page.
#Author: Tilman Oelgeschlaeger
#Last edited: 30/08/2019
#####

params = (
   ('db','parameters'),
)
#note that data values should be edited for different measurements;
#the below is just as a test input

def main():
	ser = None
	connected = False
	while True:
		try:
			print "Connecting... ",
			ser = serial.Serial("/dev/ttyACM0",9600,timeout = 1)
			print "Finished connecting"
			list = []
			while(len(list) < 6):
#				print "Reading"
				line = ser.readline(12).rstrip()
			#	print line
				if line != '':
					list.append(line)
#					print list[len(list) -1]
#				print "Done"

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
		       		terms = line.split(" ")
#				print terms[0]
       				if terms[0] == 'TV':
#    					print 'in'
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

#				print line,
        			response = requests.post('http://localhost:8086/write',params=params,data=data)
#				print response.content
   				print data
			ser.close()

main()
