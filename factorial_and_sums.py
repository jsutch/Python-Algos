def rFactorial(num):
	if num <= 1:
		return 1
	else:
		return rFactorial(num - 1) * num

for i in range(1,6):
	print rFactorial(i)

In [33]: def rsum(n):
    ...:     if n == 0:
    ...:         return 0
    ...:     return rsum(n -1) + n
    ...:

In [34]: [rsum(x) for x in range(11)]
Out[34]: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

#Iterative Factorial
for x in range(1,11):
	sum = 1
	for loop in range(1,x + 1):
		sum *= loop
	print x, sum 

#Iterative Sum
for x in range(1,6):
    sum = 0
    for loop in range(1,x + 1):
            sum += loop
    print x, sum

def iSum(num):
	mynum = num + 1
	for x in xrange(1,mynum):
		sum = 0
		for loop in xrange(1,x + 1):
			sum += loop
	return sum 

def iFac(num):
	mynum = num + 1
	for x in xrange(1,mynum):
		sum = 1
		for loop in xrange(1,x + 1):
			sum *= loop
	return sum 


