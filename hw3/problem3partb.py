#Phil Nevins
#ECE 315 Signals and Systems
#11/8/2022
#Problem 3, Part B

import numpy as np
import matplotlib.pyplot as plt

Omega = np.linspace(0, np.pi, 1024)
z = np.exp(1j*Omega)
zsqr = np.multiply(z, z)
oneVec = np.ones(np.size(z))

H = np.divide((-2.0)*zsqr + 3.0*z, (-8.0)*zsqr + 2.0*z + 1.0*oneVec)

magH = np.abs(H);
phaseH = np.angle(H);

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(Omega, magH)
ax.set_title("Magnitude of the Frequency Response $H(e^{j\Omega})$")
ax.set_ylabel("$|H(e^{j\Omega})|$")
ax.set_xlabel("Angular frequency $\Omega$")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(Omega, phaseH)
ax.set_title("Phase of the Frequency Response $H(e^{j\Omega})$")
ax.set_ylabel("Phase of $H(e^{j\Omega})$")
ax.set_xlabel("Angular frequency $\Omega$")
plt.show()