# -*- coding: utf-8 -*-
"""
Philip Nevins
10/21/2022
ECE 315 Signals & Systems
HW#2, Problem 3a
"""
import numpy as np
import matplotlib.pyplot as plt

#Period
N0 = ((326*np.pi) / 9)

#Number of periods to plot, starting from n = 0
numPeriods = 3
lastn = numPeriods*N0

#Time
n = np.arange(0, lastn + 1)

#Phase Shift
oneVec = np.ones(np.size(n)) 

#Signal
x = 2.0*np.sin(((9.0)/163.0)*n - (0.75*np.pi)*oneVec) 
fig, ax = plt.subplots(1, figsize=(15,6))
ax.stem(n, x)
ax.set_xlim([0, lastn])
ax.set_ylim([-2.25, 2.25])

#Plot Settings
ax.set_xlabel("Time $n$", fontsize='large')
ax.set_ylabel("Signal Function $x[n]$", fontsize='large')
ax.set_title("Signal $x[n]$ v Time $n$", fontsize='x-large')