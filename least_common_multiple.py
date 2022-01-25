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
"""
