# recursive/memoized example, not well optimized

def coinschange(n, coins, coinsdict=None):
    """
    coinschange(x,[1, 5, 10, 25, 50])
    gets unwieldy after 55
    """
     if coinsdict == None:
         coinsdict= {}
     if n <= 0:
         coinsdict[n] = 0
         return coinsdict[n]
     elif n in coinsdict.keys():
         return coinsdict[n]
     elif n in coins:
         coinsdict[n] = 1
         return coinsdict[n]
     else:
         _min = 0
         for c in coins:
             result = coinschange(n - c, coins)
             if result !=0:
                 if _min == 0 or (result + 1) < _min:
                     _min = 1 + result
         coinsdict[n] = _min
         return coinsdict[n]

# Can test if list order makes a difference
In [304]:  change1
Out[304]: [1, 5, 10, 25, 50]

In [305]:  change2
Out[305]: [50, 25, 10, 5, 1]


In [296]: for x in range(1,55):
     ...:     start = tstart()
     ...:     coinschange(x,[1, 5, 10, 25, 50])
     ...:     end = tend()
     ...:     print(x, end - start)
     ...:
1 4.191999323666096e-06
2 7.4929994298145175e-06
3 5.079011316411197e-06
4 6.112997652962804e-06
5 7.609924068674445e-07
6 2.825006959028542e-06
7 6.126007065176964e-06
8 1.1099997209385037e-05
9 1.795300340745598e-05
10 7.599883247166872e-07
# <...>



# dynamic example
coins = [1,5,10,25]
def change(n, coins_available, coins_so_far):
    """
    returns a generator object
    Usage:  [s for s in change(<integer of cash>, <array of coin types>, <blank or populated list of outcomes>)]
    e.g.
    [s for s in change(15, change1, [])]
    """
    if sum(coins_so_far) == n:
        yield coins_so_far
    elif sum(coins_so_far) > n:
        pass
    elif coins_available == []:
        pass
    else:
        for c in change(n, coins_available[:], coins_so_far+[coins_available[0]]):
            yield c
        for c in change(n, coins_available[1:], coins_so_far):
            yield c



In [314]: [s for s in change(15, change1, [])]
Out[314]:
[[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5],
 [1, 1, 1, 1, 1, 5, 5],
 [1, 1, 1, 1, 1, 10],
 [5, 5, 5],
 [5, 10]]

# output changes depending on the order of the coins_available values
In [320]: [s for s in change(22, change2, [])]
Out[320]: [[10, 10, 1, 1], [10, 5, 5, 1, 1], [10, 5, 1, 1, 1, 1, 1, 1, 1], [10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [5, 5, 5, 5, 1, 1], [5, 5, 5, 1, 1, 1, 1, 1, 1, 1], [5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]



