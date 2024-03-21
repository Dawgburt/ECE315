#Phil Nevins
#ECE 315 Signals and Systems
#11/28/2022
#Problem 5, Part A

import numpy as np
import matplotlib.pyplot as plt
Omega0 = (2.0*np.pi)/5.0 # fundamental angular frequency of x[n]
k = np.arange(-10, 10) # frequency indices
Omega0k = Omega0*k # Defined to prevent this from being calculated twice.


cx =(1/5.0)*(2.0 - np.exp(-1j*Omega0k)+np.exp(2.0*-1j*Omega0k) - 2.0*np.exp(3.0*-1j*Omega0k)-np.exp(4.0*-1j*Omega0k))

fig, ax = plt.subplots(1, figsize=(12,3))
ax.stem(k, np.real(cx))
ax.set_title("Four Periods of the Real Part of $c_x[k]$")
ax.set_xlabel("$k$")
ax.set_ylabel("$Re\{c_x[k]\}$")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.stem(k, np.imag(cx))
ax.set_title("Four Periods of the Imaginary Part of $c_x[k]$")
ax.set_xlabel("$k$")
ax.set_ylabel("$Im\{c_x[k]\}$")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.stem(k, np.abs(cx))
ax.set_title("Four Periods of $|c_x[k]|$")
ax.set_xlabel("$k$")
ax.set_ylabel("$|c_x[k]|$")
plt.show()

fig, ax = plt.subplots(1, figsize=(12,3))
ax.stem(k, np.angle(cx))
ax.set_title("Four Periods of the Phase of $c_x[k]$")
ax.set_xlabel("$k$")
ax.set_ylabel("$\\angle c_x[k]$")
plt.show()