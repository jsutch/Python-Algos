#!/usr/local/bin/python

# Given an array X of multiple values (e.g. [-3,5,1,3,2,10]), write a program that reverses the values in the array.  Once your program is done X should be in the reserved order.  Do this without creating a temporary array.  Also, do NOT use the reverse method but find a way to reverse the values in the array (HINT: swap the first value with the last; second with the second to last and so forth).

# note - this method will only work with arrays of an even length
#my_array = [1,2,3,4,5,6,7,8]
my_array = [-3, 3, -50, 10, 14, -2, 21, -4]
loop = 0

print my_array

for loop in range(0,len(my_array) / 2):
	temp = my_array[loop]
	# set a[0] to a[1]
	my_array[loop] = my_array[len(my_array) - 1 - loop]
	my_array[len(my_array) - 1 - loop] = temp
	print loop
	#print my_array
	loop += 1
print my_array
