#!/usr/bin/env python3

import numpy as np

x = np.array([1, 2, 3, 4, 5]); y = np.array([6, 7, 8, 9, 10])
print("x = ", x)
print("y = ", y)
z = x + y
print("z = x + y = ", z, "\n")
h = np.cos(x)
print("h = cos(x) = ", h, "\n")
t = np.linspace(0, 5, 20)
g = np.exp(1j*np.pi*t)
print("g = exp(j2*pi*t) = ", g)


