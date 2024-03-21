# -*- coding: utf-8 -*-
"""
Philip Nevins
10/21/2022
ECE 315 Signals & Systems
HW#2, Problem 3e
"""
import numpy as np
import matplotlib.pyplot as plt

#Period
N0 = (192*np.pi/5)

#Number of periods to plot, starting from n = 0
numPeriods = 1
lastn = numPeriods*N0

#Time
n = np.arange(0, lastn + 1)

#Phase Shift
oneVec = np.ones(np.size(n)) 

#Signal
x = 3.0*np.exp(((-5j*n) / 96) - (1j*np.pi/3)*oneVec) 
fig, ax = plt.subplots(1, figsize=(15,6))
ax.stem(n, x)
ax.set_xlim([0, lastn])
ax.set_ylim([-3, 3])

#Plot Settings
ax.set_xlabel("Time $n$", fontsize='large')
ax.set_ylabel("Signal Function $x[n]$", fontsize='large')
ax.set_title("Signal $x[n]$ v Time $n$", fontsize='x-large')