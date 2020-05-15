def factors(n):
    return set(reduce(list.__add__,  ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

factors(1000)

#In [130]: factors(1000)
#Out[130]: {1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000}
