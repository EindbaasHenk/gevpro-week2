#!/usr/bin/env python

import sys
import xml.etree.ElementTree as ET

	
def main(argv):
	tree = ET.parse(argv[1])
	root = tree.getroot()
			
	for point in root.findall('POINT'):
		bottomHZ = point.find('BOTTOM_HZ').text
		topHZ = point.find('TOP_HZ').text
		F0START = point.find('F0_START').text
		F0END = point.find('F0_END').text
				
		if float(F0START) < float(bottomHZ) or float(F0START) > float(topHZ) or float(F0END) < float(bottomHZ) or float(F0END) > float(topHZ):
			root.remove(point)
	
	tree.write(argv[2])
			
if __name__ == "__main__":
	main(sys.argv)
	
