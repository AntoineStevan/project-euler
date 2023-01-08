#! /usr/bin/env python3
import numpy as np

num = 0
j = 0
f = 0
while f <= 500:
    f = 0
    j += 1
    num = num + j
    for n in range(1, int(np.round(np.sqrt(num)))):
        if num % n == 0:
            f = f + 2
print(num)
