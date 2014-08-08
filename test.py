#!/bin/python

class Classo:
	task = ""
	def method1(self):
		self.task()
		print "hello"

def doSome():
	print "BACK"

c1 = Classo()
c1.task = doSome
c1.method1()