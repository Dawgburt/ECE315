# -*- coding: utf-8 -*-
"""
Philip Nevins
10/21/2022
ECE 315 Signals & Systems
HW#2, Problem 3d
"""
import numpy as np
import matplotlib.pyplot as plt

#Period
N0 = (287/4)

#Number of periods to plot, starting from n = 0
numPeriods = 1
lastn = numPeriods*N0

#Time
n = np.arange(0, lastn + 1)

#Phase Shift
oneVec = np.ones(np.size(n)) 

#Signal
x = 3.0*np.exp(((8j*np.pi*n) / 287) - (3j*np.pi/2)*oneVec) 
fig, ax = plt.subplots(1, figsize=(15,6))
ax.stem(n, x)
ax.set_xlim([0, lastn])
ax.set_ylim([-10, 10])

#Plot Settings
ax.set_xlabel("Time $n$", fontsize='large')
ax.set_ylabel("Signal Function $x[n]$", fontsize='large')
ax.set_title("Signal $x[n]$ v Time $n$", fontsize='x-large')

avgPower = np.dot(np.abs(x)[0:72],np.abs(x)[0:72])/72;
print("The average power of x[n] is {0} (furlongs / fortnite)^2.".format(avgPower))