import numpy as np
import matplotlib.pyplot as plt

# Calculate the CTFS coefficients.
NCoeffs = 50
totalNCoeffs = 2*NCoeffs + 1
omega0 = np.pi/2.0

coeffs = np.zeros(totalNCoeffs, dtype=complex)
harmonicNum = np.arange(-NCoeffs, NCoeffs + 1)
for k in harmonicNum:
    index = k + NCoeffs
    if k != 0:
        expFactor = np.exp(1j*omega0*k)
        expFactor2 = np.exp(-1j*omega0*k)
        coeffs[index] = 2.0*expFactor2/(k**2*np.pi**2) + expFactor/(k**2*np.pi**2) - 3/(k**2*np.pi**2) + 3.0*1j*expFactor2/(2.0*k*np.pi) - 1j*expFactor/(k*np.pi)
    if k == 0:
        coeffs[index] = 7.0/8.0
      
# Calculate the values of the original signal.
tx = np.linspace(0.0, 1.0, 400)
tx1 = np.linspace(-1.0, 0.0, 400) 
oneVec = np.ones(np.size(tx))
oneVec = np.ones(np.size(tx1))
x = 2.0*tx + 1.0*oneVec
x = 1.0*oneVec - tx1


# Calculate the values of the partial sums.
t = np.linspace(-2.0, 2.0, 500)
omega0jt = (1j*np.pi/2.0)*t
print("")
for N in [50]:
    xN = np.zeros(np.size(t), dtype=complex)
for k in np.arange(-N, N + 1):
    xN += coeffs[k + NCoeffs]*np.exp(k*omega0jt)
   

print("The maximum absolute value of the imaginary part of x{0}(t) is {1}."\
.format(N, np.max(np.abs(np.imag(xN)))))
    
# Plot the Nth partial sum.
fig, ax = plt.subplots(1, figsize=(12,4))
ax.plot(t, np.real(xN)) # The imaginary part should be 0.
ax.set_title("Partial sum $x_N(t)$ of CTFS for $x(t)$ when N = {0}".format(N))
ax.set_ylim([-1.0, 4.0])
ax.set_xlabel("Time t")
ax.set_ylabel("$x_{N}(t)$")

# Plot the original signal
ax.plot([-1.5, -1.0], [0.0, 0.0], color="tab:red")
ax.plot([-1.0, -1.0], [0.0, 2.0 ],color="tab:red")
ax.plot([-1.0, 0.0], [2.0, 1.0 ],  color="tab:red")
ax.plot([-1.0 , 0.0], [2.0, 1.0], color="tab:red")
ax.plot([0.0, 1.0], [1.0, 3.0], color="tab:red")
ax.plot([1.0, 1.0], [0.0, 3.0],  color="tab:red")
ax.plot([1.0 , 2.0], [0.0, 0.0], color="tab:red")
plt.show()