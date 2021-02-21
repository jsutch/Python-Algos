def rFactorial(num):
	if num <= 1:
		return 1
	else:
		return rFactorial(num - 1) * num

for i in range(1,6):
	print rFactorial(i)

def rSum(num):
	if num == 1:
		return 1
	else:
		return rSum(num -1) + num

for i in range(1,6):
	print rSum(i)

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


