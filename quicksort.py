def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)



In [715]: quicksort(myarr)
Out[715]:
[11,
 51,
 96,
 384,
 458,
 549,
 710,
 849,
 862,
 959,
 961,
 988,
 1129,
 1133,
 1241,
 1292,
 1355,
 1459,
 1496,
 1527,
 1659,
 1734,
 1756,
 1792,
 1804,
 1810,
 1860,
 1870,
 1922,
 1940,
 1983,
 2045]
