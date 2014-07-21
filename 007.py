"""
Project Euler Problem #7
=========================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6^th prime is 13.

What is the 10001^st prime number?
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

if __name__ == "__main__":
    primes = gen_prime()
    p = 0
    for i in range(10001):
        p = primes.next()
    print p
