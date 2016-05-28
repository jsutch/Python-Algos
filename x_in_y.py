#!/usr/local/bin/python

#Write a program that inserts a new number X at an index Y. For example if array = [1, 3, 5, 7] and X = 10, and Y = 2, by the end of your program array should be [1, 3, 10, 5, 7] (in other words we added '10' on index 2). Check the output of your array once your program is completed to make sure it's working correctly.

my_array = [-3, 3, 50, 10, 14, 2, 21, 4]

x = 10
y = 2

print "before" ,my_array
my_array.insert(y,x)
print "after" ,my_array