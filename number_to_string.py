#!/usr/local/bin/python

#Write a program that takes an array of numbers and replaces any number that's negative to a string called 'Dojo'. For example if array = [-1, -3, 2] after your program is done array should be ['Dojo', 'Dojo', 2].

my_array = [-3, 3, -50, 10, 14, -2, 21, -4]
loop = 0

while loop < len(my_array):
	num = my_array[loop]
	if num < 0:
		my_array[loop] = 'dojo'
	loop += 1
print my_array		