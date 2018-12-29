#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def plotspec(x, Ts):
    """ Plot time series and spectrum of x. """
    xf = (np.fft.fftshift(np.abs(np.fft.fft(x))))
    time = x.size*Ts
    t = np.arange(0,time,Ts)
    xf_axis = np.arange(-1/(2*time)*x.size, 1/(2*time)*x.size, 1/(time))
    fig = plt.figure()
    fig.subplots_adjust(hspace = 0.75)
    ax1 = fig.add_subplot(211) # 211 means, 2-by-1 grid, select plot 1
    ax1.plot(t,x)
    ax1.set_xlabel('Time (seconds)')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Signal')
    ax1.grid(True)
    ax2 = fig.add_subplot(212) # 212 means, 2-by-1 grid, select plot 2
    ax2.plot(xf_axis, xf)
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('Magnitude')
    ax2.set_title('Spectrum')
    ax2.grid(True)
    plt.show()