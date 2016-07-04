#! /usr/bin/python

import socket, sys,os,time, re

class cefGen(object):
	def __init__(self):
		#First we need a port, IP and filename!
		port, IP, filename = self.getInput()

		#We need to generate the system path!
		filename =  self.getPath() + "/" + filename
		
		#Now we start reading from the file line by line and output to a TCP port and IP
		self.readFile(filename, port, IP)

	def validatePort(self, port):
		if not port:
			sys.exit("Need to enter a valid port!")
		else:
			try:
				port = int(port)
			except:
				sys.exit("port is a numerical value!")
			
			if port > 1024:
				sys.exit("Sorry the port needs to be less than 1024!")
			else: 
				print "Port entered is " + str(port)

	def validateIP(self, IP):
		if not IP:
			sys.exit("Need to enter a valid IP!")
		else:
			IP = str(IP)
			p = re.compile('\d{1,3}')
			ipValidate = p.findall(IP)
			if len(ipValidate) != 4:
				sys.exit("invalid IP address entered!")
			for n in ipValidate:
				if int(n) > 255:
					sys.exit("invalid IP address entered!")

	def validateFilename(self, filename):
		if not filename:
			sys.exit("You need to enter a valid filename!")
		

	def outputWrite(self, output, port, IP):
		TCP_PORT = int(port)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               	s.connect((IP, TCP_PORT))
               	s.send(output)
                s.close()

	def getInput (self):
		print "Today we'll be generating a 0.33 EPS load of CEF events to a TCP socket on this host!"
                port = raw_input("What port would you like to send this load to? Remember this value can only be between 0-65535, preferably higher than 1024! ")
		self.validatePort(port)
                IP = raw_input("What is the destination IP address? ")
		self.validateIP(IP)
                filename = raw_input("What is the filename? Remember, the file should be in the same directory as this script! ")
		self.validateFilename(filename)
		return port, IP, filename


	def getPath(self):
		path = os.getcwd()
                print "Your current path is " + path
		return path

	def readFile(self, filename, port, IP):
		try:
			cefFile = open(filename)
		except:
                        sys.exit("Does file exist? Is the name valid?")

		for line in cefFile.readlines():
			print "about to print event"
			time.sleep(3)
			print line
			print "Sending event through to TCP port " + port
			try:
				self.outputWrite(line, port, IP)
			except:
				sys.exit("Either target IP or port is blocked? Maybe local machine has a firewall turned on?")
		cefFile.close()

def main():
	file = cefGen()

if __name__ == "__main__":
	main()
