#!/usr/local/bin/python3


# Daniel Lesko
# Biz-Card-OCR in Python

import os, sys
import time
import re

def readCard(bizCard):
	lines = [line.rstrip('\n') for line in open(bizCard)]

	return lines

#Checks to see if name is found anywhere in the email name, otherwise returns "Not Found"
def findName(emailAddress, data):

	sep = '@'

	emailName = emailAddress.split(sep,1)[0]

	#print(emailName)
	
	for line in data:
		words = line.split()
		#print(words)

		for word in words:
			if word.lower() in emailName.lower():
				if line != emailAddress:
					name = line
					return name

	return ("Not Found")

#Returns the first phone number found matching regex, otherwise returns "Not Found"
def findPhoneNumber(data):
	# http://stackoverflow.com/questions/3868753/find-phone-numbers-in-python-script
	phonePattern = re.compile(".*(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")

	for line in data:
		if phonePattern.match(line):
			phoneNumber = line
			phoneNumber = re.sub("\D", "", phoneNumber)
			return phoneNumber

	return ("Not Found")
	
#Returns email address matching regex, otherwise returns "Not Found"
def findEmailAddress(data):
	# http://emailregex.com/
	emailPattern = re.compile("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

	for line in data:
		if emailPattern.match(line):
			emailAddress = line
			return emailAddress

	return ("Not Found")

class Contact:
	def __init__(self, name, phoneNumber, emailAddress):
		self.name = name
		self.phoneNumber = phoneNumber
		self.emailAddress = emailAddress

	def __str__(self):
		return ("Name: %s\nPhone: %s\nEmail: %s" % (name, phoneNumber, emailAddress))
		
	



if __name__=="__main__":

	bizCard = sys.argv[1]

	data = readCard(bizCard)

	#print(data)

	phoneNumber = findPhoneNumber(data)
	emailAddress = findEmailAddress(data)
	name = findName(emailAddress, data)

	#print("Name: %s" % name)
	#print("Phone: %s" % phoneNumber)
	contact1 = Contact(name, phoneNumber, emailAddress)

	print(contact1)

	