#! /usr/bin/env python3
from utils import primes_below
from utils import primes1

import numpy as np

n = 600851475143
primes = primes1(int(np.sqrt(n)))
primes = primes[n % primes == 0]
print(n, ':', primes, "->", np.max(primes))
