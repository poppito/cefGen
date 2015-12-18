#! /usr/bin/python

import socket, sys,os,time

class cefGen(object):
	def __init__(self, filename="", output=""):
		if not filename:
			self.readFile()

	def outputWrite(self, output):
                TCP_PORT = 513
                print TCP_PORT
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('', TCP_PORT))
                s.send(output)
                s.close()

	def readFile(self):
		path = os.getcwd()
		print "path is " + path
		filename = raw_input("What is the filename?")
		filename = path + "/" + filename
		cefFile = open(filename)
		for line in cefFile.readlines():
			print "about to print line"
			time.sleep(3)
			print line
			print "Sending event through to LS"
			self.outputWrite(line)
			time.sleep(3)
		f.close()

def main():
	file = cefGen()

if __name__ == "__main__":
	main()
