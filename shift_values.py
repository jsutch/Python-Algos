#!/usr/local/bin/python


my_array = [8,3, 33, 42, 10, 14, 2, 21, 4]
loop = 0

while  loop < len(my_array):
	print(my_array)
	my_array.append(my_array[0])
	my_array.pop(0)
	print(my_array)
	loop += 1
