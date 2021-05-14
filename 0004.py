#! /usr/bin/env python3
import numpy as np

from utils import is_palindromic

n_digits = 3
n = 10**n_digits

palindromes = []
for i in range(1, n):
        for j in range(i, n):
                num = i*j
                if is_palindromic(num):
                        palindromes.append(num)

print(np.max(palindromes))
