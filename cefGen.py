#! /usr/bin/python

import socket, sys,os,time

class cefGen(object):
	def __init__(self, filename="", output=""):
		if not filename:
			self.readFile()

	def outputWrite(self, output, port):
		TCP_PORT = int(port)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('', TCP_PORT))
                s.send(output)
                s.close()

	def readFile(self):
		path = os.getcwd()
		print "path is " + path
		print "Today we'll be generating a 0.33 EPS load of CEF events to a TCP socket on this host!"
		port = raw_input("What port would you like to send this load to? Remember this value can only be between 0-65535, preferably higher than 1024! ")
		filename = raw_input("What is the filename? Remember, the file should be in the same directory as this script! ")
		filename = path + "/" + filename
		cefFile = open(filename)
		for line in cefFile.readlines():
			print "about to print event"
			time.sleep(3)
			print line
			print "Sending event through to TCP port " + port
			self.outputWrite(line, port)
		f.close()

def main():
	file = cefGen()

if __name__ == "__main__":
	main()
