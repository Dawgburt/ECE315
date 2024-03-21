# -*- coding: utf-8 -*-
"""
@author: pnevi
"""
#x = 3.0*np.exp(((-5j*n) / 96) - (1j*np.pi/3)*oneVec) 
import numpy as np
import matplotlib.pyplot as plt

lastn = 192*np.pi/5
n = np.arange(0, lastn + 1) # time vector
oneVec = np.ones(np.size(n)) # vector of ones for phase shift
phase = ((-5*n) / 96) - (np.pi/3)*oneVec
mag = 3.0

xre = mag*np.cos(phase) # real part of x[n]
xim = mag*np.sin(phase) # imag part of x[n]

fig, ax = plt.subplots(1, figsize=(15,6))
ax.stem(n, xre)
ax.set_xlim([0, lastn])
ax.set_ylim([-3.25, 3.25])
ax.set_title("Real Part of the aperiodic Signal x[n]")
ax.set_xlabel("Time n")
ax.set_ylabel("Re{x[n]}")

fig, ax = plt.subplots(1, figsize=(15,6))
ax.stem(n, xim)
ax.set_xlim([0, lastn])
ax.set_ylim([-3.25, 3.25])
ax.set_title("Imaginary Part of the aperiodic Signal x[n]")
ax.set_xlabel("Time n")
ax.set_ylabel("Im{x[n]}")