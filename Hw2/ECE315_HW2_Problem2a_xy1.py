# -*- coding: utf-8 -*-
"""
Philip Nevins
10/21/2022
ECE 315 Signals & Systems
HW#2, Problem 2a
"""
import numpy as np
import matplotlib.pyplot as plt

#Setup Plot
plt.style.use('seaborn-whitegrid')
fig, (ax1, ax2) = plt.subplots(2, figsize=(15, 5), sharex=True)

#Plot Points y1[n]
for i in range(0, 20):
    ax2.stem(i, -0.5)
ax2.stem(-1, 5)
ax2.stem(20, 5)

for i in range(-5, 0):
    ax2.stem(i, 0)
    
for i in range (20, 25):
    ax2.stem(i, 0)

#Plot Points x1[n]
for i in range(0, 20):
    ax1.stem(i, (5 - i/2))
    
for i in range(-5, 0):
    ax1.stem(i, 0)
    
for i in range (20, 25):
    ax1.stem(i, 0)
    
#Plot Settings
ax2.set_xlabel("Time $n$", fontsize='large')
ax2.set_ylabel("Signal Function $y1[n]$", fontsize='large')
ax2.set_title("Signal $y1[n]$ v Time $n$", fontsize='x-large')

ax1.set_ylabel("Signal Function $x1[n]$", fontsize='large')
ax1.set_title("Signal $x1[n]$ v Time $n$", fontsize='x-large')