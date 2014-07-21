"""
Project Euler Problem #5
=========================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

def gcd(a, b):
    if a < 0 or b < 0:
        raise ValueError('Invalid arguments. Both the values must be positive integer', a, b)
    elif a < b:
        return gcd(b, a)
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    gcd_val = gcd(a, b)
    return a * b / gcd_val

if __name__ == "__main__":
    n = 20
    ans = 2520
    for v in range(11, n, 1):
        ans = lcm(v, ans)
    print ans
