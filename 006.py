"""
Project Euler Problem #6
=========================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

def enum_pairs(ls):
    pairs = []
    n = len(ls)
    for i in range(n):
        for j in range(i+1, n):
            pairs.append((ls[i], ls[j]))
    return pairs

if __name__ == "__main__":
    n = 100
    terms = range(1, n+1)
    diff = 0
    for a, b in enum_pairs(terms):
        diff += a * b * 2
    print diff
