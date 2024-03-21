#Phil Nevins
#ECE 315 Signals and Systems
#11/8/2022
#Problem 1, Part D

import numpy as np
import matplotlib.pyplot as plt

r1 = -1/4
r2 = 1/2
c1 = -1/24
c2 = -1/12
nmin = -1;
nmax = 12;
n = np.arange(nmin, nmax + 1)
h = np.zeros(np.size(n))
zeroIdx = -nmin

for m in np.arange(0, nmax):
    if m < 1:
        h[zeroIdx + m] = -2.0*(c1*r1**m + c2*r2**m)
    elif m < 2:
        h[zeroIdx + m] = -2.0*(c1*r1**m + c2*r2**m) \
                        + 3.0*(c1*r1**(m-1) + c2*r2**(m-1))
    else:
        h[zeroIdx + m] = -2.0*(c1*r1**m + c2*r2**m) \
                        + 3.0*(c1*r1**(m-1) + c2*r2**(m-1))

phaseh = np.angle(h)

fig, ax = plt.subplots(1, figsize=(12,3))
ax.stem(n, h)
ax.set_title("Impulse Response h[n]")
ax.set_xlabel("Time n")
ax.set_ylabel("{h[n]}")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.stem(n, phaseh)
ax.set_title("The Phase of the Impulse Response h[n]")
ax.set_xlabel("Time n")
ax.set_ylabel("Phase {h[n]}")
plt.show()