#!/usr/local/bin/python

my_array = [-3, 3, 50, 10, 14, 2, 21, 4]
loop = 0
highnum = 0

while loop < len(my_array):
	num = my_array[loop]
	if highnum < num:
		highnum = num
	loop += 1
print highnum		
