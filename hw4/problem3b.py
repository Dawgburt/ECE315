#Phil Nevins
#ECE 315 Signals and Systems
#11/28/2022
#Problem 3, Part B

import numpy as np
import matplotlib.pyplot as plt

# F{x(t)} = 2/(j*omega + 1)^3
omega = np.linspace(-8.0, 8.0, 2000)
oneVec = np.ones(np.size(omega))
factor = 1.0 + 1j*omega
X = np.divide(6.0*oneVec,np.multiply(np.multiply(factor,factor),np.multiply(factor,factor)))

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(omega, np.real(X))
ax.set_title("Real Part of $X(j\\omega)$")
ax.set_xlabel("Angular Frequency $\\omega$")
ax.set_ylabel("$Re\\{X(j\\omega)\\}$")
plt.savefig("prob3b_real_python.png")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(omega, np.imag(X))
ax.set_title("Imaginary Part of $X(j\\omega)$")
ax.set_xlabel("Angular Frequency $\\omega$")
ax.set_ylabel("$Im\\{X(j\\omega)\\}$")
plt.savefig("prob3b_imag_python.png")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(omega, np.abs(X))
ax.set_title("Magnitude of $X(j\\omega)$")
ax.set_xlabel("Angular Frequency $\\omega$")
ax.set_ylabel("$|X(j\\omega)|$")
plt.savefig("prob3b_mag_python.png")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(omega, np.angle(X))
ax.set_title("Phase of $X(j\\omega)$")
ax.set_xlabel("Angular Frequency $\\omega$")
ax.set_ylabel("$\\angle X(j\\omega)$")
plt.savefig("prob3b_phase_python.png")
plt.show()