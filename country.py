#!/usr/bin/env python

import sys


class country():
	
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return "{} {}".format("Hello from", self.name)
		
def main(argv):
	hoi = country(argv[1])
	print(hoi)
	
if __name__ == "__main__":
	main(sys.argv)
	
	
