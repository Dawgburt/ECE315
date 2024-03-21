# -*- coding: utf-8 -*-
"""
@author: phil nevins
"""
#x = 3.0*np.exp((((2j*np.pi)/253.0) - (np.pi/48)*oneVec)*n) 
import numpy as np
import matplotlib.pyplot as plt

lastn = 75
n = np.arange(0, lastn + 1) # time vector
oneVec = np.ones(np.size(n)) # vector of ones for phase shift
phase = (((2*n*np.pi)/253.0)*oneVec)
mag = np.exp(-n*np.pi/48)

xre = 3.0*mag*np.cos(phase) # real part of x[n]
xim = 3.0*mag*np.sin(phase) # imag part of x[n]

fig, ax = plt.subplots(1, figsize=(15,6))
ax.stem(n, xre)
ax.set_xlim([0, lastn])
ax.set_ylim([0, 3.25])
ax.set_title("Real Part of the aperiodic Signal x[n]")
ax.set_xlabel("Time n")
ax.set_ylabel("Re{x[n]}")

fig, ax = plt.subplots(1, figsize=(15,6))
ax.stem(n, xim)
ax.set_xlim([0, lastn])
ax.set_ylim([0, 0.5])
ax.set_title("Imaginary Part of the aperiodic Signal x[n]")
ax.set_xlabel("Time n")
ax.set_ylabel("Im{x[n]}")
