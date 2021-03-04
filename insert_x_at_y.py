

def x_at_y(arr,n, i):
    """
    given an array, insert 'x' element at position 'y', preserving order
	x  = n, y = i
    """
    arr.append(0)
    for z in range(len(arr) - 1, i, -1):
       myarr[z] = myarr[z - 1]
       myarr[i] = n
    return myarr
...:




"""
In [110]: myarr = [random.randint(1,101) for x in range(11)]

In [111]: print(myarr)
[60, 25, 90, 92, 92, 61, 25, 14, 7, 90, 60]

In [113]: myarrnew = x_at_y(myarr,666666,4)

In [114]: myarrnew
Out[114]: [60, 25, 90, 92, 666666, 92, 61, 25, 14, 7, 90, 60]
"""

