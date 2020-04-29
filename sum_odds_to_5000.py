#!/usr/local/bin/python

#Write a program that would print the sum of all the odd numbers from 1 to 5000

nums = 0
for num in range(0,5001):
	if num % 2 == 0:
		pass
	else: 	
		#print num
		nums += num
print(nums)