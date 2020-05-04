#!/usr/local/bin/python
import random

#Bubble Sort in python
#new test
#my_list = [10,21,4,12,33,2,1,27,40]
#my_list = [9,8,7,6,5,4,3,2,1]
my_list =[]

for num in range(1,10):
	my_list.append(random.randrange(1,10000))

loop = 0
x = 0
temp = 0

print("Original List", my_list)
for loop in range(len(my_list) -1, 0, -1):
	for x in range(loop):
		#print "Loop number" , loop, "Iteration", x
		#print "Compare", my_list[x], my_list[x+1]
		if my_list[x] > my_list[x + 1]:
			temp = my_list[x]
			my_list[x] = my_list[x + 1]
			my_list[x+1] = temp
		#print my_list	
print("Sorted List", my_list)