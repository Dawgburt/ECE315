#Phil Nevins
#ECE 315 Signals and Systems
#11/8/2022
#Problem 1, Part D

import numpy as np
import matplotlib.pyplot as plt

# Nonzero portions of h and x
h = [3, 2, 1];
x = [0, 1, -2, 2, -1, 0];

# Times when x*h is possibly nonzero
# These are known from the earlier parts of Problem 1.
n = np.arange(-2,6);
y = np.convolve(x,h);

fig, ax = plt.subplots(1, figsize=(12,3))

ax.stem(n, y)
ax.set_ylim([-4, 4])
ax.set_title("Output from the NumPy function convolve")
ax.set_xlabel("n")
ax.set_ylabel("conv(x,h)")
ax.grid(True)