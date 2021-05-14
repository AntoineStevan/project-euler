#! /usr/bin/env python3


def fact(n: int) -> int:
    """ Computes the factorial of n. """
    if n <= 1:
        return 1

    p = 1
    for i in range(2, n+1):
        p *= i
    return p


n = 100
f = fact(n)

print(f"{n}! = {f} ->", sum([int(char) for char in str(f)]))
