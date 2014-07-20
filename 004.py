"""
Project Euler Problem #4
=========================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math

def list_combs(n):
    a = n / 2
    b = n - a
    ls = []
    while a >= 0:
        ls.append((a, b))
        a = a - 1
        b = b + 1
    return ls

def gen_combs(n):
    i = 0
    while i <= n:
        for a, b in list_combs(i):
            yield (n - a) * (n - b), (n - a), (n - b)
        i = i + 1

def is_palindromic(n):
    s = str(n)
    return s == s[::-1]

if __name__ == "__main__":
    n = 999
    combs = gen_combs(n)
    ans = -1
    for v, a, b in combs:
        if (a >= 100 and b >= 100 and is_palindromic(v) and v > ans):
            ans = v
    print ans
