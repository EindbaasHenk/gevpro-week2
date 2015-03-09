#!/usr/bin/env python

import sys

import json

from collections import namedtuple

def main(argv):
	#opening json file in program (read)
	inputfile = open(argv[1], 'r')
	json_corpus = json.load(inputfile)
	
	#create output (write)
	outputfile = open(argv[2], "w")
	
	#json object become named tuples
	tuple_json = namedtuple("tuple_json", ["naam", "classificatie", "bloed", "sterven"])
	
	#looping through blood-die.json and create output if bloed=sterven
	for word_object in json_corpus:
		
		word_tuple = tuple_json(word_object[0], word_object[1], word_object[2], word_object[3])
		bloed = word_tuple.bloed.split()
		sterven = word_tuple.sterven.split()
		
		[json.dump(word_object, outputfile) for bloed in bloed if bloed in sterven]
	
	#close the opened files	
	inputfile.close()
	outputfile.close()
	
if __name__ == "__main__":
	main(sys.argv)
