#!/bin/python

import sys
import socket

# the -c switch is for the client to connect to the hosting ip
#python client.py -c -h 127.0.0.1 -p 5001

# the -b switch binds the host ip and port
#python client.py -b -h 127.0.0.1 -p 5001

# host must initialize first before client can connect with the host

#TODO: MUST implement a way for host to send msgs as well

args = sys.argv
argumentLen = len(sys.argv)

for num in range(1,argumentLen):
	if args[num] == "-b":
		setup = args[num]
	else:
		setup = "-c"

	if args[num] == "-h":
		ip = args[num+1]
	if args[num] == "-p":
		port = int(args[num+1])

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

loop = True
if(setup == "-b"):
	s.bind((ip, port))
	while loop:
		data, addr = s.recvfrom(1024)
		if data == "end":
			s.close()
			break
		print "Received: ", data
else:
	while loop:
		received = raw_input(">")
		s.sendto(received, (ip, port))
		if received == "end":
			s.close()
			break

print "Connection Closed"
