#!/usr/local/bin/python

#Given an array of multiple values (e.g. [0, -1, 2, -3, 4, -5, 6]), write a program that removes any negative values in that array.  Once your program is done, the array should be composed of only the non-negative numbers, in their original order.  Do this without creating a temporary array; only use the pop() method to remove values from the array.

my_array = [-3, 3, -50, 10, 14, -2, 21, -4]
#my_array = [-11,2,3,4,5,6,7,-1]

def removeNegs(array):
	loop = 0
	print("Original Array is" ,my_array)
	while loop < len(my_array):
		#print loop	
		if my_array[loop] < 0:
			my_array.remove(my_array[loop])
		#print my_array
		loop += 1	
	print("Anti-Negative array is: ", my_array)


removeNegs(my_array)


# Simpler method with list comprehension
In [192]: my_array = [-3, 3, -50, 10, 14, -2, 21, -4]

In [193]: [x for x in my_array if x > 0]
Out[193]: [3, 10, 14, 21]

