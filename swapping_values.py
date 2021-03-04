#!/usr/local/bin/python


# Write a program that takes an array of numbers and returns an array where the first and last numbers in the array have been switched.For example say x = [2, 3, 5, 7, 6]. By the end of the program x, should be [6, 3, 5, 7, 2]. Do this without creating an empty array.

my_array = [-3, 3, 50, 10, 14, 2, 21, 4]

print(my_array)

last = len(my_array) - 1 
temp = my_array[0]
my_array[0] = my_array[last]
my_array[last] = temp

print(my_array)

# as a function with some bounds checking
In [155]: myarr
Out[155]: [53, 32, 38, 61, 57, 44, 90, 81, 26, 15, 69]

In [157]: def swap_values(x, y, arr):
     ...:     if (x < len(arr)) and (y < len(arr)) and (x !=y):
     ...:         arr[x],arr[y] = arr[y],arr[x]
     ...:         return arr
     ...:     else:
     ...:         return 'Indexes must be smaller than the array and not the same'
     ...:
     ...:
     ...:

In [158]: swap_values(22,6,myarr)
Out[158]: 'Indexes must be smaller than the array and not the same'

In [159]: swap_values(6,6,myarr)
Out[159]: 'Indexes must be smaller than the array and not the same'

In [160]: swap_values(2,8,myarr)
Out[160]: [53, 32, 26, 90, 57, 44, 61, 81, 38, 15, 69]
