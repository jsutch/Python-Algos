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
   return n * (n -1) / 2

"""
example of numbers of connections needed for a full mesh
In [38]: [symkey(x) for x in range(33)]
Out[38]:
[0.0,
 0.0,
 1.0,
 3.0,
 6.0,
 10.0,
 15.0,
 21.0,
 28.0,
 36.0,
 45.0,
 55.0,
 66.0,
 78.0,
 91.0,
 105.0,
 120.0,
 136.0,
 153.0,
 171.0,
 190.0,
 210.0,
 231.0,
 253.0,
 276.0,
 300.0,
 325.0,
 351.0,
 378.0,
 406.0,
 435.0,
 465.0,
 496.0]
"""
