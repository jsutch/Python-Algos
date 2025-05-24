def ipmax(n):
    """total ip addresses in a mas:  2^ 32bits - n is total, remove two for broadcast and gateway """
    return f"total usable IP addresses for a mask of /{n} mask", (2 **(32 - n) - 2 )


"""
an example
In [36]: [ipmax(x) for x in range(33)]
Out[36]:
[('total usable IP addresses for a mask of /0 mask', 4294967294),
 ('total usable IP addresses for a mask of /1 mask', 2147483646),
 ('total usable IP addresses for a mask of /2 mask', 1073741822),
 ('total usable IP addresses for a mask of /3 mask', 536870910),
 ('total usable IP addresses for a mask of /4 mask', 268435454),
 ('total usable IP addresses for a mask of /5 mask', 134217726),
 ('total usable IP addresses for a mask of /6 mask', 67108862),
 ('total usable IP addresses for a mask of /7 mask', 33554430),
 ('total usable IP addresses for a mask of /8 mask', 16777214),
 ('total usable IP addresses for a mask of /9 mask', 8388606),
 ('total usable IP addresses for a mask of /10 mask', 4194302),
 ('total usable IP addresses for a mask of /11 mask', 2097150),
 ('total usable IP addresses for a mask of /12 mask', 1048574),
 ('total usable IP addresses for a mask of /13 mask', 524286),
 ('total usable IP addresses for a mask of /14 mask', 262142),
 ('total usable IP addresses for a mask of /15 mask', 131070),
 ('total usable IP addresses for a mask of /16 mask', 65534),
 ('total usable IP addresses for a mask of /17 mask', 32766),
 ('total usable IP addresses for a mask of /18 mask', 16382),
 ('total usable IP addresses for a mask of /19 mask', 8190),
 ('total usable IP addresses for a mask of /20 mask', 4094),
 ('total usable IP addresses for a mask of /21 mask', 2046),
 ('total usable IP addresses for a mask of /22 mask', 1022),
 ('total usable IP addresses for a mask of /23 mask', 510),
 ('total usable IP addresses for a mask of /24 mask', 254),
 ('total usable IP addresses for a mask of /25 mask', 126),
 ('total usable IP addresses for a mask of /26 mask', 62),
 ('total usable IP addresses for a mask of /27 mask', 30),
 ('total usable IP addresses for a mask of /28 mask', 14),
 ('total usable IP addresses for a mask of /29 mask', 6),
 ('total usable IP addresses for a mask of /30 mask', 2),
 ('total usable IP addresses for a mask of /31 mask', 0),
 ('total usable IP addresses for a mask of /32 mask', -1)]

"""


def symkey(n):
   """Sum of n Natural Numbers - total number of connections required in a full mesh"""
   return f"required symmetric keys for {n} nodes", n * (n -1) / 2

"""
In [4]: [symkey(x) for x in range(33)]
Out[4]:
[('required symmetric keys for 0 nodes', 0.0),
 ('required symmetric keys for 1 nodes', 0.0),
 ('required symmetric keys for 2 nodes', 1.0),
 ('required symmetric keys for 3 nodes', 3.0),
 ('required symmetric keys for 4 nodes', 6.0),
 ('required symmetric keys for 5 nodes', 10.0),
 ('required symmetric keys for 6 nodes', 15.0),
 ('required symmetric keys for 7 nodes', 21.0),
 ('required symmetric keys for 8 nodes', 28.0),
 ('required symmetric keys for 9 nodes', 36.0),
 ('required symmetric keys for 10 nodes', 45.0),
 ('required symmetric keys for 11 nodes', 55.0),
 ('required symmetric keys for 12 nodes', 66.0),
 ('required symmetric keys for 13 nodes', 78.0),
 ('required symmetric keys for 14 nodes', 91.0),
 ('required symmetric keys for 15 nodes', 105.0),
 ('required symmetric keys for 16 nodes', 120.0),
 ('required symmetric keys for 17 nodes', 136.0),
 ('required symmetric keys for 18 nodes', 153.0),
 ('required symmetric keys for 19 nodes', 171.0),
 ('required symmetric keys for 20 nodes', 190.0),
 ('required symmetric keys for 21 nodes', 210.0),
 ('required symmetric keys for 22 nodes', 231.0),
 ('required symmetric keys for 23 nodes', 253.0),
 ('required symmetric keys for 24 nodes', 276.0),
 ('required symmetric keys for 25 nodes', 300.0),
 ('required symmetric keys for 26 nodes', 325.0),
 ('required symmetric keys for 27 nodes', 351.0),
 ('required symmetric keys for 28 nodes', 378.0),
 ('required symmetric keys for 29 nodes', 406.0),
 ('required symmetric keys for 30 nodes', 435.0),
 ('required symmetric keys for 31 nodes', 465.0),
 ('required symmetric keys for 32 nodes', 496.0)]
"""
