#!/usr/local/bin/python
"""
shift values one position to the right.
In this cast you wind up with the same final array
"""

my_array = [8,3, 33, 42, 10, 14, 2, 21, 4]
loop = 0

while  loop < len(my_array):
	print(my_array)
	my_array.append(my_array[0])
	my_array.pop(0)
	print(my_array)
	loop += 1

# doing something more useful, as a function:
In [161]: myarr
Out[161]: [ 53, 32, 26, 90, 57, 44, 61, 81, 38, 15, 69]

In [162]: def prepend_to_array(arr,n):
     ...:     arr.append(0)
     ...:     for x in range(len(arr) -1,-1,-1):
     ...:         arr[x] = arr[x -1]
     ...:     arr[0] = n
     ...:     return arr
     ...:

In [163]: prepend_to_array(myarr,2222)
Out[163]: [2222, 53, 32, 26, 90, 57, 44, 61, 81, 38, 15, 69]


# the pythonic way:
In [181]: myarr.insert(0,4444)

In [182]: myarr
Out[182]: [4444, 2222, 53, 32, 26, 90, 57, 44, 61, 81, 38, 15, 69]

