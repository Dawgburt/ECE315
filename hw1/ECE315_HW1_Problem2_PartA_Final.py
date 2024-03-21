# -*- coding: utf-8 -*-
"""
Philip Nevins
10/2/2022
ECE 315 Signals & Systems
"""
import numpy as np
import matplotlib.pyplot as plt

#Amplitude and Fundamental Period
H = 2 #Max Amp
h = 1 #Min Amp
T0 = 2 #Fundamental Period

#Axis Parameters
tmin = -6
tmax = 6
t = np.arange(tmin, tmax + 1)

#Setup Plot
plt.style.use('seaborn-whitegrid')
fig, ax = plt.subplots(1, figsize=(15, 5))

#Plot Points
for i in range(tmin, tmax, T0):
    p0 = i
    p1 = i + T0 / 2
    p2 = i + T0
    
    plt.scatter([p0, p1, p2], [h, h, H], ec='b', fc='b')
    plt.scatter([p0, p2], [H, H], ec='b', fc='none')

    
    plt.plot([p0, p1, p2], [h, h, H], color='b', ls='-') #Solid Line
    plt.plot([p2, p2], [h, H], color='b', ls='--') #Dashed Line
    
#Plot Settings
plt.xlabel("Time $t$", fontsize='large')
plt.ylabel("Signal Function $x(t)$", fontsize='large')
plt.title("Signal $x(t)$ v Time $t$", fontsize='large')