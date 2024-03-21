#Phil Nevins
#ECE 315 Signals and Systems
#11/28/2022
#Problem 6, Part C

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftshift

Omega = np.linspace(-np.pi, np.pi, 1000)
oneVec = np.ones(np.size(Omega))

X = 2.0*oneVec - np.cos(Omega) - 3j*np.sin(Omega)

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(Omega, np.abs(X))
ax.set_xlabel("Angular Frequency $\\Omega$")
ax.set_ylabel("$|X(e^{j\\Omega})|$")
ax.set_title("Magnitude of the Fourier Transform of $x[n]$")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(Omega, np.angle(X))
ax.set_xlabel("Angular Frequency $\\Omega$")
ax.set_ylabel("$\\angle X(e^{j\\Omega})$")
ax.set_title("Phase of the Fourier Transform of $x[n]$")
plt.show()

L = 1024
x = [-2.0,2.0,1.0]
z = np.zeros(L, dtype=complex)

for n in np.arange(0,3):
    z[n] = x[n]
    OmegaL = -np.pi + np.arange(0,L)*(2.0*np.pi/L)
    xfft = fftshift(fft(z))

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(OmegaL, np.abs(xfft))
ax.set_xlabel("Angular Frequency $\\Omega$")
ax.set_ylabel("Magnitude of the FFT of $x$")
ax.set_title("Magnitude of the FFT of $x$ vs $\\Omega$")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.plot(OmegaL, np.angle(xfft))
ax.set_xlabel("Angular Frequency $\\Omega$")
ax.set_ylabel("Phase of the FFT of $x$")
ax.set_title("Phase of the FFT")
plt.show()

Y = np.multiply(np.exp(2j*OmegaL),xfft)
fig, ax = plt.subplots(1, figsize=(12,3))
magX, = ax.plot(Omega, np.abs(X), label="$|X(e^{j\\Omega})|$", linestyle="-")
magY, = ax.plot(OmegaL, np.abs(Y), label="$|Y(e^{j\\Omega})|$", linestyle=":")
ax.set_xlabel("Angular Frequency $\\Omega$")
ax.set_ylabel("$|Y(e^{j\\Omega})|$")
ax.set_title("Magnitude of the Frequency Shifted FFT")
ax.legend(handles=[magX, magY])
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
angX, = ax.plot(Omega, np.angle(X), label="$\\angle X(e^{j\\Omega})$",\
linestyle="-")
angY, = ax.plot(OmegaL, np.angle(Y), label="$\\angle Y(e^{j\\Omega})$",\
linestyle=":")
ax.set_ylim([-4, 4])
ax.set_xlabel("Angular Frequency $\\Omega$")
ax.set_ylabel("$\\angle Y(e^{j\\Omega})$")
ax.set_title("Phase of the Frequency Shifted FFT")
ax.legend(handles=[angX, angY])
plt.show()