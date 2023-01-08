#! /usr/bin/env python3
import numpy as np

numbers = np.arange(1000)
multiples = numbers[(numbers % 3 == 0) + (numbers % 5 == 0)]
print(np.sum(multiples))
