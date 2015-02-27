#!/usr/bin/env python

import sys
import json
from collections import namedtuple

def main(argv):
	inputData= open(argv[1],'r')
	outputFile=open('blood-die_identical.json','w')
	activeFile = json.load(inputData)
	CountryInfo =namedtuple('Countryinfo', 'country, classification, blood, dying')
	for line in activeFile:
		currentTuple = CountryInfo(line[0],line[1],line[2], str(line[3]).rstrip()) #.rstrip() verwijdert \n
		bloodWords = currentTuple.blood.split(',')
		dyingWords = currentTuple.dying.split(',')
		[json.dump(currentTuple, outputFile, indent=0) for blood in bloodWords if blood in dyingWords]
	inputData.close()
	outputFile.close()
		
		
if __name__ == "__main__":
	main(sys.argv)

