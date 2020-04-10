#Python EXIF extraction#

import sys
import os

def dir_listing():
	
	dir = raw_input("Enter The Directory Containing The Files e.g. ./Evidence : ")
	print "Method One - os.walk"
	file_list = []
	for path, subdirs, files in os.walk(dir):
		for filename in files:
			f = os.path.join(path, filename)
			print f

	print "\nMethod Two - os.listdir"
	for fn in os.listdir(dir):
			file_name = os.path.join(dir,fn)
			print file_name

dir_listing()