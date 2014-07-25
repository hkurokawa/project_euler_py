"""
Project Euler Problem #3
=========================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import math

def is_prime(n, prime_nums_list):
    """Return True if the given number is not divisible
    by any number in the list. Return False otherwise."""
    for v in prime_nums_list:
        # If the next prime number is greater than sqrt(n),
        # it means that n is prime.
        if v > math.sqrt(n):
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

def find_largest_prime_factor(num):
    """Return the largest prime factor of the given number."""
    prime = gen_prime()
    while True:
        p = prime.next()
        # If the next prime number is greater than num / 2,
        # it means that num is prime. So just return num itself.
        if p > num / 2:
            return num
        if num % p == 0:
            q = num / p
            return max(p, find_largest_prime_factor(q))

if __name__ == "__main__":
    n = 600851475143
    print find_largest_prime_factor(n)
