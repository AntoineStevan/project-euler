#! /usr/bin/env python3
from math import comb

n = 1000

s = sum([int(digit) for digit in str(2**n)])

print(s)