#!/usr/local/bin/python

my_array = [-3, 3, 50, 10, 14, 2, 21, 4]
loop = 0
sum = 0

while loop < len(my_array):
	num = my_array[loop]
	#print num
	sum += num
	#print sum
	loop += 1
avg = (sum / len(my_array))
print(avg)	