#Phil Nevins
#ECE 315 Signals and Systems
#11/8/2022
#Problem 3, Part C

import numpy as np
import matplotlib.pyplot as plt

from scipy import signal

a = [-8.0, 2.0, 1.0]
b = [-2.0, 3.0]

w, H = signal.freqz(b, a, 1024)
magH = np.abs(H);
phaseH = np.angle(H);

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(w, magH)
ax.set_title("Magnitude of the Frequency Response $H(e^{j\Omega})$")
ax.set_ylabel("$|H(e^{j\Omega})|$")
ax.set_xlabel("Angular frequency $\Omega$")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(w, phaseH)
ax.set_title("Phase of the Frequency Response $H(e^{j\Omega})$")
ax.set_ylabel("Phase of $H(e^{j\Omega})$")
ax.set_xlabel("Angular frequency $\Omega$")
plt.show()