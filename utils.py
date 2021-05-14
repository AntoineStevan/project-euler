import numpy as np
from numpy import ndarray
from numpy import arange as nparange

from typing import List


def primes_below(n: int) -> ndarray:
    """
            Computes all the primes strictly below the given integer.

            :param n: the upper bound of the primes to be computed.
            :return: an array containing all the primes strictly below n.
    """
    assert isinstance(n, int), f"n is supposed to be an integer but {n} was given."
    primes = nparange(2, n)
    for i in range(2, n):
        primes[(primes % i == 0) * (primes > i)] = 0
    return primes[primes > 0]


def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return np.array([2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]])


def is_palindromic(n: int) -> bool:
    """ Tells if n is a palindromic number. """
    n = str(n)
    p = len(n)
    head = n[:p // 2]
    tail = n[p // 2:] if p % 2 == 0 else n[p // 2 + 1:]
    return head == tail[::-1]


def divisors(n: int) -> np.ndarray:
    """ Gives the list of the divisors of n. """
    # compute the primes below the square root of n.
    divs = np.arange(1, n + 1)
    return divs[n % divs == 0]


def longest_path(_triangle: List[List[int]]) -> int:
    """ Computes the longest path from top to bottom in the triangle. """

    def aux(t):
        rows = len(t)
        if rows == 1:
            return t[0][0]  # assuming a triangle with depth 1 is of the form [*]

        left = [t[row][:-1] for row in range(1, rows)]
        right = [t[row][1:] for row in range(1, rows)]

        return t[0][0] + max(aux(left), aux(right))

    return aux(_triangle)
