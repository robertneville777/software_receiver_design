#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 22:24:34 2018

@author: clintschad
"""

import numpy as np
import matplotlib.pyplot as plt

t_sim = 1
fs = 100
x = np.arange(0,t_sim,1/fs)

y = np.sin(2*np.pi*10*x) + 0.5*np.cos(2*np.pi*5*x)
yf = 20*np.log10(np.fft.fftshift(np.abs(np.fft.fft(y))))
xf = np.arange(-1/(2*t_sim)*y.size, 1/(2*t_sim)*y.size, 1/(t_sim))

fig = plt.figure()
fig.subplots_adjust(hspace = 0.75)
ax1 = fig.add_subplot(211) # 211 means, 2-by-1 grid, select plot 1
ax1.plot(x,y)
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Amplitude')
ax1.set_title('Cosine Waves')
ax1.grid(True)
ax2 = fig.add_subplot(212) # 212 means, 2-by-1 grid, select plot 2
ax2.plot(xf, yf)
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Magnitude (dB)')
ax2.set_title('Spectrum of Cosine Waves')
ax2.grid(True)
plt.show()