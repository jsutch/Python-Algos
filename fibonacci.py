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