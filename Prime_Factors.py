def primeFactors(n):
    """
    return the prime factors of n
    """
    pfarr =  []
    while n % 2 ==0:
        pfarr.append(2)
        n = n / 2 # n must be odd
    for i in range(3, int(math.sqrt(n))+2, 2):
        while n % i == 0:
            pfarr.append(i)
            n = n / i
    if n > 2:
        pfarr.append(2)
    return pfarr

#In [129]: primeFactors(1000)
#Out[129]: [2, 2, 2, 5, 5, 5]
primeFactors(1000)
