#Phil Nevins
#ECE 315 Signals and Systems
#11/8/2022
#Problem 5, Part C

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

a = [2.0, -5.0, -7]
b = [-3.0, 0.0, 11.0]

w, H = signal.freqs(b, a, worN=np.linspace(-10.0, 10.0, 1024))

magH = np.abs(H);
phaseH = np.angle(H);

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(w, magH)
ax.set_title("Magnitude of the Frequency Response $H(j\omega)$ from freqz")
ax.set_ylabel("$|H(j\omega)|$")
ax.set_xlabel("Angular frequency $\omega$")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(w, phaseH)
ax.set_title("Phase of the Frequency Response $H(j\omega)$ from freqz")
ax.set_ylabel("Phase of $H(j\omega)$")
ax.set_xlabel("Angular frequency $\omega$")
plt.show()