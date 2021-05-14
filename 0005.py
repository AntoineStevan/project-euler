#! /usr/bin/env python3
import numpy as np

n = 20

divisors = np.arange(1,n+1)

for i in range(len(divisors)):
        for j in range(i+1, len(divisors)):
                if divisors[j] % divisors[i] == 0:
                        divisors[j] = divisors[j] / divisors[i]

print(n, np.prod(divisors))
