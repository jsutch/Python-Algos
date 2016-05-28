#!/usr/local/bin/python

my_array = [-3, 3, -50, 10, 14, -2, 21, -4]
loop = 0


while loop < len(my_array):
	num = my_array[loop]
	if num < 0:
		my_array[loop] = 0
	loop += 1
print my_array	