#!/usr/bin/env python

import sys

def main(argv):
	output_file_name = argv[2]
	import xml.etree.ElementTree as ET
	tree = ET.parse('spontal.xml')
	root = tree.getroot()
	for point in root.findall('POINT'):
		b_hz = float(point.find('BOTTOM_HZ').text)
		t_hz = float(point.find('TOP_HZ').text)
		f0_st = float(point.find('F0_START').text)
		f0_e = float(point.find('F0_END').text)
		if f0_st > t_hz or f0_st < b_hz:
			root.remove(point)
		elif f0_e > t_hz or f0_e <b_hz:
			root.remove(point)
	tree.write(output_file_name)
	
if __name__ == "__main__":
	main(sys.argv)
		
