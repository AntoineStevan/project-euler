#! /usr/bin/env python3
import numpy as np


def sum_of_divisors(n: int) -> int:
    """ Computes of the proper divisors of n. """
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s


def is_amicable_pair(a: int, da: int, b: int, db: int) -> bool:
    """ Tells if the pair of integer is an amicable one, i.e. if da = b & db = a with a != b. """
    return a != b and da == b and db == a


n = 10_000
s_divs = np.zeros(shape=n, dtype=int)
for i in range(n):
    s_divs[i] = sum_of_divisors(i+1)

amicable = np.zeros(shape=n, dtype=int)
for i in range(len(s_divs)):
    for j in range(i+1, len(s_divs)):
        if is_amicable_pair(i+1, s_divs[i], j+1, s_divs[j]):
            print(i+1, j+1)
            amicable[i] = 1
            amicable[j] = 1

print(np.sum(np.arange(1, n+1) * amicable))
