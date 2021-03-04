#!/usr/local/bin/python

mylist=[1, 3, 5, 7, 9, 13]
loop=0

while loop < len(mylist):
	print(mylist[loop])
	loop += 1

# more pythonic:
[x for x in mylist]
