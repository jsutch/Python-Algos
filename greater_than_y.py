#!/usr/local/bin/python

my_array = [-3, 3, 50, 10, 14, 2, 21, 4]
output = []
loop = 0
y = 8

while loop < len(my_array):
	num = my_array[loop]
	if num > y:
		output.append(num)
	loop += 1

print("from the list", my_array, "only" , output ,"are greater than", y)

# slightly cleaner:
In [142]: n=66
In [143]: output = []
     ...: for x in range(0,len(myarr)):
     ...:     if myarr[x] < n:
     ...:         output.append(myarr[x])
     ...:

In [148]: print(f'only {output} are greater than {n} in {myarr}')
only [60, 25, 61, 25, 14, 7, 60] are greater than 66 in [60, 25, 90, 92, 92, 61, 25, 14, 7, 90, 60]


# as function return indexes as well -python3
In [136]: def greater_than(arr,n):
     ...:     """
     ...:     find if a given integer is larger than other integers in an array.
     ...:     return indexes and the numbers if true, False if not
     ...:     """
     ...:     biggers = {}
     ...:     for i in range(0,len(arr)):
     ...:         if n > arr[i]:
     ...:             biggers[i] = arr[i]
     ...:     if biggers:
     ...:         return biggers
     ...:     else:
     ...:         False
     ...:
     ...:

In [137]: greater_than(myarr,66)
Out[137]: {0: 60, 1: 25, 6: 61, 7: 25, 8: 14, 9: 7, 11: 60}

In [138]: myarr
Out[138]: [60, 25, 90, 92, 666666, 92, 61, 25, 14, 7, 90, 60]

In [139]: myarr.pop(4)
Out[139]: 666666

In [140]: myarr
Out[140]: [60, 25, 90, 92, 92, 61, 25, 14, 7, 90, 60]

In [141]: greater_than(myarr,66)
Out[141]: {0: 60, 1: 25, 5: 61, 6: 25, 7: 14, 8: 7, 10: 60}
