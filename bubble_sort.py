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


===============

another loop
import RandArray

myarr = RandArray.RandIntArray()

print(myarr)

# as a function
for loop in range(len(myarr) -1, -1, -1):
	for x in range(loop):
            if myarr[x] > myarr[x + 1]
		temp = myarr[x]
		myarr[x] = myarr[x + 1]
		myarr[x + 1] = temp
print(myarr)

# even simpler using assignments:
In [199]: def bubble(arr):
     ...:     for loop in range(len(arr) -1, -1, -1):
     ...:         #print(loop)
     ...:         for x in range(loop):
     ...:             if arr[x] > arr[x + 1]:
     ...:                 arr[x], arr[x + 1] = arr[x + 1], arr[x]
     ...:     return arr[-1]



