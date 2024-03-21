# -*- coding: utf-8 -*-
"""
Philip Nevins
10/21/2022
ECE 315 Signals & Systems
HW#2, Problem 2c
"""
import numpy as np
import matplotlib.pyplot as plt

#Setup Plot
plt.style.use('seaborn-whitegrid')
fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 5), sharex=True)

#Plot Points y2[m]
for i in range(0, 20):
    ax2.stem(i, -0.5)
ax2.stem(-1, 5)
ax2.stem(20, 5)
for i in range(-5, -1):
    ax2.stem(i, 0)
for i in range(21, 26):
    ax2.stem(i, 0)

#Plot Points x[n]
for i in range(0, 20):
    ax1.stem(i, (4 - i/2))
ax1.stem(-1, 5)
ax1.stem(20, 0)
    
for k in range(-5, -1):
    ax1.stem(k, 0)
    
for j in range (21, 25):
    ax1.stem(j, 0)
    
#Plot Settings
ax2.set_xlabel("Time $m$", fontsize='large')
ax2.set_ylabel("Signal Function $y2[m]$", fontsize='large')
ax2.set_title("Signal $y2[m]$ v Time $m$", fontsize='x-large')

ax1.set_ylabel("Signal Function $xTilda[n]$", fontsize='large')
ax1.set_title("Signal $xTilda[n]$ v Time $n$", fontsize='x-large')