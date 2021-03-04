#!/usr/local/bin/python

my_array = [-3, 3, -50, 10, 14, -2, 21, -4]
loop = 0


while loop < len(my_array):
	num = my_array[loop]
	if num < 0:
		my_array[loop] = 0
	loop += 1
print(my_array)	


# with list comprehension:
In [325]: def neg_to_zero(n):
     ...:     if n < 0:
     ...:         return 0
     ...:     else:
     ...:         return n
     ...:

In [326]: [neg_to_zero(x) for x in my_array]
Out[326]: [0, 3, 0, 10, 14, 0, 21, 0]
