#!/usr/local/bin/python

my_array = [8,3, 33, 42, 10, 14, 2, 21, 4]
loop = 0
total = 0
maxint = ''
min = ''

while loop < len(my_array):
	if maxint == '':
		maxint = my_array[loop]
	if min == '':
		min = my_array[loop]
	num = my_array[loop]
	total += num
	if num > maxint:
		maxint = num
	if num < min:
		min = num	
	loop += 1

print "Max is" , maxint
print "Min is", min
print "Average is" , sum(my_array)/len(my_array)	