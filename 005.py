"""
Project Euler Problem #5
=========================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

def is_prime(n, prime_nums_list):
    """Return True if the given number is not divisible
    by any number in the list. Return False otherwise."""
    for v in prime_nums_list:
        # If the next prime number is greater than n / 2,
        # it means that n is prime.
        if v > n / 2:
            return True
        if n % v == 0:
            return False
    return True

def gen_prime():
    """Return a prime number generator."""
    prime_nums_list = []
    num = 2
    while True:
        if is_prime(num, prime_nums_list):
            prime_nums_list.append(num)
            yield num
        num = num + 1

def list_primes(max_num):
    primes = gen_prime()
    ls = []
    for i in primes:
        if i > max_num:
            break
        ls.append(i)
    return ls

def prime_factorise(n, prime_nums_list):
    if n == 1:
        return dict()
    for p in prime_nums_list:
        if n % p == 0:
            factors = prime_factorise(n / p, prime_nums_list)
            if not p in factors:
                factors[p] = 1
            else:
                factors[p] = factors[p] + 1
            return factors
    raise ValueError('The given number is not divisible with the given prime numbers list', n, prime_nums_list)

if __name__ == "__main__":
    n = 20
    primes = list_primes(n)
    sum_factors = dict()
    for i in range(2, n, 1):
        factors = prime_factorise(i, primes)
        for k, v in factors.items():
            if not k in sum_factors:
                sum_factors[k] = 1
            elif sum_factors[k] < v:
                sum_factors[k] = v
    ans = 1
    for v, f in sum_factors.items():
        while f > 0:
            ans = ans * v
            f = f - 1
    print ans
