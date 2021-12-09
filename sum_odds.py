#!/usr/local/bin/python

#Write a program that would print the sum of all the odd numbers from 1 to 5000

nums = 0
for num in range(0,1000):
	if num % 2 == 0:
		pass
	else: 	
		nums += num
print(nums)#!/usr/local/bin/python

#Write a program that would print the sum of all the odd numbers from 1 to 5000

nums = 0
for num in range(0,5001):
	if num % 2 == 0:
		pass
	else: 	
		nums += num
print(nums)


# 
def sumodds(n):
	"""
	sum odds to n. use _sum to not clash with the sum() function
	"""
	_sum = 0
	for x in range(1,n + 1):
		if not x %2 == 0:
			_sum += x
    return _sum


In [202]: sumodds(200)
Out[202]: 10000

In [203]: sumodds(66)
Out[203]: 1089

In [204]: sumodds(10)
Out[204]: 25

In [205]: 1 + 3 + 5 + 7 + 9
Out[205]: 25

# can also use builtins and list comprehension:
In [210]: sum([x for x in range(10) if x %2 !=0])
Out[210]: 25

