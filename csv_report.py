#!/usr/local/bin/python

import csv

users = {}

with open('mycsv.csv', 'rU') as csv_file:
	reader = csv.reader(csv_file)
	labels = reader.next()
	booklist = []


	for row in reader:
		# create  2-tuple list from two lists - labels and row (proto dictionary)
		entry = zip(labels, row)
		#print entry # prints full entry - debugging
		#update the list
		booklist.append(entry)
		#create a dictionary called addressbook from the  2-tuple list form of entry
		addressbook = dict(entry)
		# extract the values from addressbook using the list[name]
		# this will now print First Name and Last Name
		print '{a[first_name]} {a[last_name]}'.format(a=addressbook)

	for label in labels:
		# pulls in the values from label and addressbook in the format of "label: value" with newline and ------ between records
		print "{}: {} \n".format(label, addressbook[label])
	print "---------------------------"	