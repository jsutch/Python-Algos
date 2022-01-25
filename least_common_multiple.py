 def lcm(a:int,b:int,limit:int=10):
    """
    simple function to calculate the least common multiple of two numbers
    - has an upper limit defaulted to 10
    """
     aarr = []
     barr = []
     for loop in range(1,limit + 1):
         aarr.append( a * loop)
         barr.append(b * loop)
     myarr = set(aarr) & set(barr)
     try:
         if min(myarr):
             return(min(myarr))
     except Exception as e:
         return None


"""
In [68]: lcm(8,10)
Out[68]: 40

In [69]: print(lcm(8,10))
40

In [70]: print(lcm(2,5))
10

In [71]: print(lcm(3,5))
15

In [72]: print(lcm(6,9))
18

In [85]: for x,y in zip(range(1,101),range(101,1,-1)):
    ...:     print(f'{x} and {y} have a least common multiple of {lcd(x,y,100)} up to a limit of 100')
    ...:
    ...:
1 and 101 have a least common multiple of None up to a limit of 100
2 and 100 have a least common multiple of 100 up to a limit of 100
3 and 99 have a least common multiple of 99 up to a limit of 100
4 and 98 have a least common multiple of 196 up to a limit of 100
5 and 97 have a least common multiple of 485 up to a limit of 100
6 and 96 have a least common multiple of 96 up to a limit of 100
7 and 95 have a least common multiple of 665 up to a limit of 100
<...>
"""
