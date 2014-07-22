"""
Project Euler Problem #9
=========================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

def ceil(a):
    return int(math.ceil(a))

def floor(a):
    return int(math.floor(a))

def list_triplet(n):
    sqrt_2 = math.sqrt(2)
    ls = []
    # As a + b > c and a + b + c = n, c < n/2.
    # Also, c > n/3 because c > a (c^2 > a^2), c > b (c^2 > b^2) and a + b + c = n
    for c in range(ceil(n/3.0), floor(n/2.0) + 1):
        # Here, we can assume a < b.
        # Hence, b > c / sqrt(2) and b > (n - c) / 2
        for b in range(int(max(c / sqrt_2, ceil((n - c) / 2.0))), c):
            a = n - c - b
            # a < c / sqrt(2) and c < (n - c) / 2
            if a < c / sqrt_2 and a <= (n - c) / 2:
                ls.append((a, b, c))
    return ls

if __name__ == "__main__":
    n = 1000
    for a, b, c in list_triplet(n):
        if a * a + b * b == c * c:
            print a * b * c
            break
    else:
        print "Pythagorean triplet not found for", n
                
