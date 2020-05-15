def primes_sieve(limit):
    """
    for each number in an array, if it has factors other than 1 or itself, remove it from the list
    """
    mylimit = limit+1
    primes = list(range(2, mylimit))
    
    for i in primes:
        factors = range(i, mylimit, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes

print(primes_sieve(1338))
