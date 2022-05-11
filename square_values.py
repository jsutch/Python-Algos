#!/usr/local/bin/python

my_array = [-3, 3, 50, 10, 14, 2, 21, 4]
loop = 0

while loop < len(my_array):
	num = my_array[loop]
	print("The Square of", num ,"is" , num * num)
	loop += 1


# more pythonic as a function, called by a list comprehension
In [190]: def square(n):
     ...:     return n **2
     ...:

In [191]: [square(x) for x in my_array]
Out[191]: [9, 9, 2500, 100, 196, 4, 441, 16]



# the more pythonic way with a lambda/map
In [189]: list(map(lambda x: x**2, my_array))
Out[189]: [9, 9, 2500, 100, 196, 4, 441, 16]

# a square function using a lambda
In [149]: square = lambda x: x ** 2
In [150]: [square(x) for x in range(11)]
Out[150]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

