# recursive solution
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n -1) + fib(n-2)


# In [9]: [fib(x) for x in range(20)]
# Out[9]:
# [0,
#  1,
#  1,
#  2,
#  3,
#  5,
#  8,
#  13,
#  21,
#  34,
#  55,
#  89,
#  144,
#  233,
#  377,
#  610,
#  987,
#  1597,
#  2584,
#  4181]

def iterfib(n):
    if n < 2:
        return n
    # track a and a + b to n
    a=1
    b=1
    for i in range(2,n):
        a, b = b, a + b
    return b

# In [12]: [iterfib(x) for x in range(20)]
# Out[12]:
# [0,
#  1,
#  1,
#  2,
#  3,
#  5,
#  8,
#  13,
#  21,
#  34,
#  55,
#  89,
#  144,
#  233,
#  377,
#  610,
#  987,
#  1597,
#  2584,
#  4181]


def memofib(n):
    """
    wrapper
    """
    return memofibber(n, {0: 0, 1: 1})

def memofibber(n, fibs):
    """
    worker
    """
    if n not in fibs:
        fib1 = memofibber(n-1, fibs)
        fib2 = memofibber(n-2, fibs)
        fibs[n] = fib1 + fib2
    return fibs[n]


def memofib(n):
    """
    this is the wrapper function:

    memoization - much faster for larger numbers than iteration
    recursion (fib(n-1) + fib(n-2) fails with numbers as low as 100
    """
    return memofibber(n, {0: 0, 1: 1})

def memofibber(n, fibs):
    """
    worker
    """
    if n not in fibs:
        fib1 = memofibber(n-1, fibs)
        fib2 = memofibber(n-2, fibs)
        fibs[n] = fib1 + fib2
    return fibs[n]
"""
In [37]: times = {}
    ...: for x in [10,100,1000]:
    ...:     begin = tstart()
    ...:     iterfib(x)
    ...:     end = tend()
    ...:     times['iter-'+str(x)] = end - begin
    ...:     begin = tstart()
    ...:     memofib(x)
    ...:     end = tend()
    ...:     times['memo-'+str(x)] = end - begin
    ...:     

In [38]: times
Out[38]: 
{'iter-10': 3.370999365870375e-06,
 'memo-10': 7.916999493318144e-06,
 'iter-100': 7.34999957785476e-06,
 'memo-100': 4.768599956150865e-05,
 'iter-1000': 7.786300011503045e-05,
 'memo-1000': 0.0008214979998228955}

"""
