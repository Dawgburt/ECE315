#Phil Nevins
#ECE 315 Signals and Systems
#11/8/2022
#Problem 5, Part B

import numpy as np
import matplotlib.pyplot as plt

omega = np.linspace(-10.0, 10.0, 2000)
jomega = 1j*omega
omega2 = np.multiply(jomega, jomega)
oneVec = np.ones(np.size(omega))

H = np.divide(-3.0*omega2 + 11.0*oneVec, 2.0*omega2 - 5.0*jomega - 7.0*oneVec)

magH = np.abs(H);
phaseH = np.angle(H);

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(omega, magH)
ax.set_title("Magnitude of the Frequency Response $H(j\omega)$")
ax.set_ylabel("$|H(j\omega)|$")
ax.set_xlabel("Angular frequency $\omega$")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(omega, phaseH)
ax.set_title("Phase of the Frequency Response $H(j\omega)$")
ax.set_ylabel("Phase of $H(j\omega)$")
ax.set_xlabel("Angular frequency $\omega$")
plt.show()
