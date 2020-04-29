#!/usr/local/bin/python

my_array = [-3, 3, 50, 10, 14, 2, 21, 4]
output = []
loop = 0
y = 8

while loop < len(my_array):
	num = my_array[loop]
	if num > y:
		output.append(num)
	loop += 1

print("from the list", my_array, "only" , output ,"are greater than", y)