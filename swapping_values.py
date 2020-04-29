#!/usr/local/bin/python


# Write a program that takes an array of numbers and returns an array where the first and last numbers in the array have been switched.For example say x = [2, 3, 5, 7, 6]. By the end of the program x, should be [6, 3, 5, 7, 2]. Do this without creating an empty array.

my_array = [-3, 3, 50, 10, 14, 2, 21, 4]

print(my_array)

last = len(my_array) - 1 
temp = my_array[0]
my_array[0] = my_array[last]
my_array[last] = temp

print(my_array)