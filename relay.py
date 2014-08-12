#!/bin/python

import socket
import threading
import signal
import sys
import time

PORT_NUMBER = 5019
# HOSTNAME = "" # Real IP ADDRESS
HOSTNAME = "127.0.0.1" # localhost
# HOSTNAME = socket.gethostname()

class P2P:
	connections = []
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def startListening(self):
		self.sock.bind((HOSTNAME, PORT_NUMBER))
		self.sock.listen(5)
		
		print "Started Listening at hostname: ", HOSTNAME
		counter = 0
		while 1:
			connectionTuple = self.sock.accept()
			singleConnection = Process(counter, "Thread:", counter, self.connections)
			singleConnection.publicEndPoint(connectionTuple)
			singleConnection.start()

			self.connections.append(singleConnection)
			counter += 1

	def __del__(self):
		self.sock.close()
		print "SOCKETS CLOSED"


class Process(threading.Thread):
	# phoneNumber is included in the P2P class dynamically 
	# public end point is the global IP address that the server will see
	def publicEndPoint(self, tupleData):
		self.client = tupleData[0]
		self.public_ip 		= tupleData[1][0]
		self.public_port 	= tupleData[1][1]

	# private end point is the IP address behind the NAT
	def privateEndPoint(self, tupleData):
		self.private_ip 		= tupleData[1][0]
		self.private_port	 	= tupleData[1][1]

	def __init__(self, threadID, name, counter, connections):
		threading.Thread.__init__(self)
		self.threadID 	= threadID
		self.name 		= name
		self.counter 	= counter
		self.connections = connections

	def run(self):
		print "Started client thread id: ", self.threadID
		print "Public IP: ", self.public_ip
		print "Puclic Port: ", self.public_port
		while 1:
			clientResponse = self.client.recv(1024)

			self.task(clientResponse)
			# if the return value is some FIN json, then end
			if (clientResponse == "end\n"):
				break
			print clientResponse
		self.client.close()
		print "Closed client"

	def task(self, input):
		# loop through connections to see if the user is in array
		# if not in array, then add user while the user waits for the 
		# other person to find 'em
		print "FIND USER"

		# if an error should occur, close connection and return YES
		# return 1

# USE CTRL-C to have this process end and then the __del__ method in P2P gets
# called because the object is released from memory inside __main__
def processEnded(signal, frame):
	print "\n"
	sys.exit(0)

if __name__ == "__main__":
	signal.signal(signal.SIGINT, processEnded) # ctrl-z
	signal.signal(signal.SIGTERM, processEnded) # terminate
	p2p = P2P()
	p2p.startListening()