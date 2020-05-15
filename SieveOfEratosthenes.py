def primes_sieve(limit):
    mylimit = limit+1
    primes = list(range(2, mylimit))
    
    for i in primes:
        factors = range(i, mylimit, i)
        for f in factors[1:]:
            if f in primes:
                primes.remove(f)
    return primes

print(primes_sieve(1338))
