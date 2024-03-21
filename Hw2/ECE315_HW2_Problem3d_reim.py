# -*- coding: utf-8 -*-
"""
@author: pnevi
"""
#x = 3.0*np.exp(((8j*np.pi*n) / 287) - (3j*np.pi/2)*oneVec) 
import numpy as np
import matplotlib.pyplot as plt

lastn = 287/4
n = np.arange(0, lastn + 1) # time vector
oneVec = np.ones(np.size(n)) # vector of ones for phase shift
phase = (((8*np.pi*n) / 287) - (3*np.pi/2)*oneVec)
mag = 3

xre = mag*np.cos(phase) # real part of x[n]
xim = mag*np.sin(phase) # imag part of x[n]

fig, ax = plt.subplots(1, figsize=(15,6))
ax.stem(n, xre)
ax.set_xlim([0, lastn])
ax.set_ylim([-3.25, 3.25])
ax.set_title("Real Part of the periodic Signal x[n]")
ax.set_xlabel("Time n")
ax.set_ylabel("Re{x[n]}")

fig, ax = plt.subplots(1, figsize=(15,6))
ax.stem(n, xim)
ax.set_xlim([0, lastn])
ax.set_ylim([-3.25, 3.25])
ax.set_title("Imaginary Part of the periodic Signal x[n]")
ax.set_xlabel("Time n")
ax.set_ylabel("Im{x[n]}")