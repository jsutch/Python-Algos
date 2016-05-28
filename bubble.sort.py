#!/usr/local/bin/python


my_list = [10,21,4,12,33,2,1,27,40]

loop = 0
iter = 0

print my_list
for iter in range(0,len(my_list) -1):
	print "Iteration", iter
	for loop in range(0,len(my_list) -1):
		print "Comparing", my_list[loop], my_list[loop +1]
		if my_list[loop] > my_list[loop +1]:
			temp = my_list[loop +loop]
			my_list[loop +1] = my_list[loop]
			my_list[loop] = temp
			print my_list