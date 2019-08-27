import serial
import numpy as np
import requests

#####
#Code to write data output from Arduino Uno into the
#InfluxDB database. Important values are data and params,
#which determine where/ the query is sent and what tags
#the read data is assigned. Note that as of now the code assumes only
#one voltage value from one source is being sent out. This will be
#extended to send all measured parameters from the Arduino to the database
#
#Author: Tilman Oelgeschlaeger
#Last edited: 27/08/2019
#####

params = (
   ('db','parameters'),
)
#note that data values should be edited for different measurements;
#the below is just as a test input

count = 0
type = 'voltage,' #should eventually change depending on measurement
data = '' #appended depending on measurement parameter

connected = True
ser = None

def main():
	while True:
		try:
			ser = serial.Serial("/dev/ttyACM0",9600,timeout = 1)
		except serial.SerialException:
			print("Device disconnected.")
			connected = False
		if connected:
	      		line = ser.readline()
  	   	 	if line != '' and line != "Voltage Reader":
				line.rstrip()
	       			terms = line.split(" ")
#				print terms[0]
       				if terms[0] == 'TV':
#	    				print 'in'
            				data = type + 'source=top value=' + terms[1]
            			elif terms[0] == 'MV':
            				data = type + 'source=middle value=' + terms[1]
				elif terms[0] == 'BV':
       					data = type + 'source=bottom value=' + terms[1]
				else:
            				continue
#				print data
        			response = requests.post('http://localhost:8086/write',params=params,data=data)
#				print response.content
       			print line,

main()
