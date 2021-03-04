#!/usr/local/bin/python

#Write a program that takes an array of numbers and replaces any number that's negative to a string. For example if array = [-1, -3, 2] after your program is done array should be ['somestring', 'somestring', 2].

my_array = [-3, 3, -50, 10, 14, -2, 21, -4]
loop = 0

while loop < len(my_array):
	num = my_array[loop]
	if num < 0:
		my_array[loop] = 'somestring'
	loop += 1
print(my_array)		


#  slightly more interesting. we'll replace the negative numbers with the "negative <string of num>" output

In [212]: numdict = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}

In [213]: my_array = [-3, 3, -4, 10, 6, -2, 9, -4]

In [216]: for x in my_array:
     ...:     if x < 0:
     ...:         print('negative',numdict[abs(x)])
     ...:
negative three
negative four
negative two
negative four

In [226]: for x in range(0,len(my_array)):
     ...:     if my_array[x] < 0:
     ...:         my_array[x] = 'negative' + numdict[abs(my_array[x])]
     ...:

In [227]: my_array
Out[227]: ['negativethree', 3, 'negativefour', 10, 6, 'negativetwo', 9, 'negativefour']

# and as a function:
In [228]: def replace_negatives(arr):
     ...:      numdict = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}
     ...:      for x in range(0,len(arr)):
     ...:          if arr[x] < 0:
     ...:              arr[x] = 'negative' + numdict[abs(arr[x])]
     ...:      return arr
     ...:

In [229]: myarr
Out[229]: [4444, 2222, 53, 32, 26, 90, 57, 44, 61, 81, 38, 15, 69]

In [230]: myarr = [random.randint(-10,11) for x in range(20)]

In [231]: replace_negatives(myarr)
Out[231]:
[2,
 8,
 11,
 'negativeeight',
 'negativefive',
 'negativeeight',
 'negativeone',
 6,
 'negativesix',
 9,
 10,
 5,
 'negativefour',
 'negativefour',
 4,
 5,
 'negativeeight',
 9,
 6,
 6]


