#Phil Nevins
#ECE 315 Signals and Systems
#11/28/2022
#Problem 5, Part B

import numpy as np
import matplotlib.pyplot as plt
N0 = 5 # fundamental period of x[n]
Omega0 = 2.0*np.pi/N0 # fundamental angular frequency of x[n]
k0 =-2 # initial frequency index
k = np.arange(k0, k0 + N0) # frequency indices
Omega0k = Omega0*k # Defined to prevent this from being calculated three times.
cx =(1/5.0)*(2.0 - np.exp(-1j*Omega0k)+np.exp(2.0*-1j*Omega0k) - 2.0*np.exp(3.0*-1j*Omega0k)-np.exp(4.0*-1j*Omega0k))
w = np.exp(-1j*Omega0k)
x = np.zeros(N0, dtype=complex)
for n in np.arange(k0, k0 + N0):
    wn = np.power(w, n)
    idx = n - k0
    x[idx] = np.dot(cx, wn)
print("The max absolute value of the imaginary part of x[n] is {0}"\
.format(np.max(np.abs(np.imag(x)))))
fig, ax = plt.subplots(1, figsize=(12,4))
ax.stem(k, np.real(x)) # the time indices n are the same as the freq indices k
ax.set_title("One Period of the Signal $x[n]$ with DTFS Coefficients $c_x[k]$")
ax.set_xlabel("$n$")
ax.set_ylabel("$x[n]$")
ax.grid(True)
plt.show()