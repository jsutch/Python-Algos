#!/usr/local/bin/python

import csv

users = {}

with open('mycsv1.csv', 'rU') as csv_file:
	reader = csv.reader(csv_file) # csv.reader is a function in the csv module
	labels = next(reader) # reader.next() is a function in the csv.reader function
	booklist = [] # make a new, empty list called booklist

	for row in reader:
		# print(row) # debugging
		entry = list(zip(labels, row)) # create  2-tuple list from two lists - labels and row (proto dictionary)
		booklist.append(entry) #update the list 'booklist'
		addressbook = dict(entry) #create a dictionary called addressbook from the  2-tuple list form of entry
		print('{a[first_name]} {a[last_name]}'.format(a=addressbook)) # this will now print First Name and Last Name columns
		for label in labels:
			print("{}: {} \n".format(label, addressbook[label]))
		print("------------------------------")


