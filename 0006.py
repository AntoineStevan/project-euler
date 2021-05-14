#! /usr/bin/env python3
import numpy as np

n = 100

s1 = n*(n+1)//2
s2 = n*(n+1)*(2*n+1)//6
print(n, s1**2-s2)
