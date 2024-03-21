#Phil Nevins
#ECE 315 Signals and Systems
#11/28/2022
#Problem 1, Part B

import numpy as np
import matplotlib.pyplot as plt
numPosCoeffs = 50
totalNumCoeffs = 2*numPosCoeffs + 1
omega0 = np.pi/2.0

c0 = 1j*omega0
cneg = -1j*omega0

coeffs = np.zeros(totalNumCoeffs, dtype=complex)
harmNum = np.arange(-numPosCoeffs, numPosCoeffs + 1)
for k in harmNum:
    index = k + numPosCoeffs
    if k != 0:
        expFactor = np.exp((c0*k))
        expFactorNeg = np.exp(cneg*k)
        coeffs[index] = 2.0/(c0*k) * expFactor - np.multiply(1/(c0*k),1/(c0*k)) * (1-expFactor) - 3*(1/(c0*k) * expFactorNeg) + 2 * np.multiply(1/(c0*k),1/(c0*k)) * (expFactorNeg - 1)
    if k == 0:
        coeffs[index] = 7.0/8.0 + 0.0*1j
        
minIdx = -20 + numPosCoeffs
maxIdx = 20 + numPosCoeffs + 1

fig, ax = plt.subplots(1, figsize=(12,3))
ax.stem(harmNum[minIdx:maxIdx], np.real(coeffs[minIdx:maxIdx]))
ax.set_title("Real Part of $c_{x}[k]$")
ax.set_xlabel("Harmonic Number $k$")
ax.set_ylabel("$Re\\{c_{x}[k]\\}$")
ax.grid("True")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.stem(harmNum[minIdx:maxIdx], np.imag(coeffs[minIdx:maxIdx]))
ax.set_title("Imaginary Part of $c_{x}[k]$")
ax.set_xlabel("Harmonic Number $k$")
ax.set_ylabel("$Im\\{c_{x}[k]\\}$")
ax.grid("True")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.stem(harmNum[minIdx:maxIdx], np.abs(coeffs[minIdx:maxIdx]))
ax.set_title("Magnitude of $c_{x}[k]$")
ax.set_xlabel("Harmonic Number $k$")
ax.set_ylabel("$|c_{x}[k]|$")
ax.grid("True")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.stem(harmNum[minIdx:maxIdx], np.angle(coeffs[minIdx:maxIdx]))
ax.set_title("Phase of $c_{x}[k]$")
ax.set_xlabel("Harmonic Number $k$")
ax.set_ylabel("$\\angle c_{x}[k]$")
ax.grid("True")
plt.show()