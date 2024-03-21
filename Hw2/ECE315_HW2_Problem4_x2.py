# -*- coding: utf-8 -*-
"""
Philip Nevins
10/21/2022
ECE 315 Signals & Systems
HW#2, Problem 4, x2[n]
"""

import numpy as np
import matplotlib.pyplot as plt

lastn = 38
n = np.arange(0, lastn + 1) # time vector
oneVec = np.ones(np.size(n)) # vector of ones for phase shift
phase = ((207*np.pi*n) / 51) - (np.pi/12)*oneVec
mag = 6.0

xre = mag*np.cos(phase) # real part of x2[n]
xim = mag*np.sin(phase) # imag part of x2[n]

fig, ax = plt.subplots(1, figsize=(15,6))
ax.stem(n, xre)
ax.set_xlim([0, lastn])
ax.set_ylim([-6.25, 6.25])
ax.set_title("Real Part of Signal x2[n]")
ax.set_xlabel("Time n")
ax.set_ylabel("Re{x2[n]}")

fig, ax = plt.subplots(1, figsize=(15,6))
ax.stem(n, xim)
ax.set_xlim([0, lastn])
ax.set_ylim([-6.25, 6.25])
ax.set_title("Imaginary Part of Signal x2[n]")
ax.set_xlabel("Time n")
ax.set_ylabel("Im{x2[n]}")