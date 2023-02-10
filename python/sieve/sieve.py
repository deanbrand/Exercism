from math import sqrt


def primes(limit):
    sieve = list(range(limit + 1))

    last = int(sqrt(limit))
    for prime in sieve[2:last + 1]:
        if prime == 0:
            continue

        comp = prime * 2
        while comp <= limit:
            sieve[comp] = 0
            comp += prime
            
    all_primes = [num for num in sieve[2:] if num != 0]
    return all_primes


print(primes(10))
