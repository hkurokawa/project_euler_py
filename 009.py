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

def _range(a, b):
    return range(ceil(a), floor(b) + 1)

def list_triplet(n):
    root_2 = math.sqrt(2)
    ls = []
    for c in _range(n/3.0, n/2.0):
        for b in range(int(max(c / root_2, ceil((n - c) / 2.0))), c):
            ls.append((n - c - b, b, c))
    return ls

if __name__ == "__main__":
    n = 1000
    for a, b, c in list_triplet(n):
        if a * a + b * b == c * c:
            print a * b * c
            break
    else:
        print "Pythagorean triplet not found for", n
                
