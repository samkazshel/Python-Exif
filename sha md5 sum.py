import os
import subprocess

items = os.listdir("C:\Users\schmu\Desktop\Assignment 2 CyberSecurity\Timeline Photos")

newlist = []
for names in items:
	if names.endswith(".jpg"):
        	newlist.append(names)
#print newlist
for img in newlist:
	subprocess.call(["shasum","images/"+img])