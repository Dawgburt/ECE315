#Phil Nevins
#ECE 315 Signals and Systems
#11/8/2022
#Problem 4, Part E

import numpy as np
import matplotlib.pyplot as plt

numpts = 2000
t = np.linspace(-2.0, 3.0, numpts)
y = np.zeros(np.size(t))

for m in np.arange(0, numpts+1):
    if t[m] <= -1.0:
            continue
    elif t[m] <= 0.0:
            y[m] = (pow(t[m], 4.0) / 12.0) - pow(t[m], 2.0) - ((2.0 * t[m]) / 3.0) + (1.0 / 4.0)
    elif t[m] <= 1.0:
            y[m] = (1.0 / 4.0) - ((2.0 * t[m]) / 3.0)
    elif t[m] <= 2.0:
            y[m] = (-(pow(t[m], 4.0) / 12.0)) + pow(t[m], 2.0) - ((4.0 * t[m]) / 3.0)
    else:
            break

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(t,y)
ax.set_xlabel("Time t")
ax.set_ylabel("y(t)")
ax.set_title("The output of the system y(t) = x(t)*h(t)")
plt.show()