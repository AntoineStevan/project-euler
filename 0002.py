#! /usr/bin/env python3
import numpy as np

fib_seq = [1,2]
while fib_seq[-1] < 4e6:
        fib_seq.append(fib_seq[-2] + fib_seq[-1])
fib_seq = np.array(fib_seq)

even_valued_sum = np.sum(fib_seq[fib_seq % 2 == 0])
print(even_valued_sum)
