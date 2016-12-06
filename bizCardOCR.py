#!/usr/local/bin/python3


# Daniel Lesko
# Biz-Card-OCR in Python

import os, sys
import time
import re

def readCard(bizCard):
	lines = [line.rstrip('\n') for line in open(bizCard)]

	return lines

def getName(emailAddress, data):

	sep = '@'

	emailName = emailAddress.split(sep,1)[0]

	#print(emailName)
	
	for line in data:
		words = line.split()
		#print(words)

		for word in words:
			if word.lower() in emailName:
				if line != emailAddress:
					name = line
					return name

def getPhoneNumber(data):
	# http://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script
	phonePattern = re.compile(".*(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")

	for line in data:
		if phonePattern.match(line):
			phoneNumber = line

	phoneNumber = re.sub("\D", "", phoneNumber)

	return phoneNumber

def getEmailAddress(data):
	# http://emailregex.com/
	emailPattern = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

	for line in data:
		if emailPattern.match(line):
			emailAddress = line

	return emailAddress

if __name__=="__main__":

	bizCard = sys.argv[1]

	data = readCard(bizCard)

	#print(data)

	phoneNumber = getPhoneNumber(data)
	emailAddress = getEmailAddress(data)
	name = getName(emailAddress, data)

	print("Name: %s" % name)
	print("Phone: %s" % phoneNumber)
	print("Email: %s" % emailAddress)

	