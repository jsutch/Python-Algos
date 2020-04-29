#!/usr/bin/env python
import RandArray

myarr = RandArray.RandIntArray()

print(myarr)
for loop in range(len(myarr) -1, -1, -1):
	for x in range(loop):
            if myarr[x] > myarr[x + 1]
		temp = myarr[x]
		myarr[x] = myarr[x + 1]
		myarr[x + 1] = temp
print(myarr)
