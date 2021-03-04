#!/usr/local/bin/python
import random

#Create an array X and fill the array with 10 values, each value being a random integer between 0 to 100.  For example when your program is done, X could be something like this: [35, 15, 3, 39, 53, 93, 25, 39, 59, 21].Create an array X and fill the array with 10 values, each value being a random integer between 0 to 100.  For example when your program is done, X could be something like this: [35, 15, 3, 39, 53, 93, 25, 39, 59, 21].

my_array = []

for loop in range(0,9):
	num = random.randrange(1,100)
	my_array.append(num)
	loop += 1
print(my_array)	


# a more pythonic way to do this with list comprehension
myarr = [random.randint(1,101) for x in range(11)]
