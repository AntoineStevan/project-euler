#! /usr/bin/env python3
import numpy as np


def collatz(_n: int) -> int:
    """ Gives the length of the collatz sequence starting from n. """
    _length = 1
    while _n > 1:
        _n = _n // 2 if _n % 2 == 0 else 3 * _n + 1
        _length += 1
    return _length


longest = (0, 0)
for n in range(1, 1_000_001):
    length = collatz(n)
    if length > longest[1]:
        longest = [n, length]
    if n % 10000 == 0:
        print(n/1_000_000*100)

print(longest)
