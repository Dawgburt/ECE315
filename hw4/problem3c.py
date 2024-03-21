#Phil Nevins
#ECE 315 Signals and Systems
#11/28/2022
#Problem 3, Part C

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift
N = 262144
T = 100.0
Ts = T/N # sample period
fs = 1.0/Ts # sample rate
df = fs/N # = 1/T = frequency increment

n = np.arange(0,N)
t = Ts*n
x = np.multiply(t*t*t,np.exp(-t))
X = fftshift(Ts*fft(x))
k = np.arange(-N/2,N/2)
omega = 2.0*np.pi*df*k

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(omega, np.real(X))
ax.set_xlim([-8.75, 8.75])
ax.set_title("Real Part of the DFT of $x(t)$")
ax.set_xlabel("Angular Frequency $\\omega$")
ax.set_ylabel("$Re\\{X(j\\omega)\\}$")
plt.savefig("prob3c_real_python.png")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(omega, np.imag(X))
ax.set_xlim([-8.75, 8.75])
ax.set_title("Imaginary Part of the DFT of $x(t)$")
ax.set_xlabel("Angular Frequency \omega")
ax.set_ylabel("$Im\\{X(j\omega)\\})$")
plt.savefig("prob3c_imag_python.png")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(omega, np.abs(X))
ax.set_xlim([-8.75, 8.75])
ax.set_title("Magnitude of the DFT of $x(t)$")
ax.set_xlabel("Angular Frequency $\\omega$")
ax.set_ylabel("$|X(j\\omega)|$")
plt.savefig("prob3c_mag_python.png")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(omega, np.angle(X))
ax.set_xlim([-8.75, 8.75])
ax.set_title("Phase of the DFT of $x(t)$")
ax.set_xlabel("Angular Frequency $\\omega$")
ax.set_ylabel("$\\angle X(j\\omega)$")
plt.savefig("prob3c_phase_python.png")
plt.show()