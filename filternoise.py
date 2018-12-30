#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Listing 3.4: Filter a noisy signal three ways. (Page 47)
"""

import numpy as np
import scipy.signal as sp
import srd as srd

time = 3
fs = 10000
Ts = 1/fs
x = np.random.randn(time*fs)
srd.plotspec(x,Ts)
#
#freqs = 0.5*fs*np.array([0,0.2,0.21,1])
#amps =  np.array([1,0]) # remez uses values in the band, not at the points
#b = sp.remez(100, freqs, amps, fs=fs)
#ylp = sp.lfilter(b,1,x)
#srd.plotspec(ylp,Ts)
#
#freqs = 0.5*fs*np.array([0, 0.24, 0.26, 0.5, 0.51, 1])
#amps =  np.array([0,1,0]) # remez uses values in the band, not at the points
#b = sp.remez(100, freqs, amps, fs=fs)
#ybp = sp.lfilter(b,1,x)
#srd.plotspec(ybp,Ts)

freqs = np.array([0, 2000, 3000, 5000])
amps =  np.array([0,1]) # remez uses values in the band, not at the points
b = sp.remez(100, freqs, amps, fs=fs)
yhp = sp.lfilter(b,1,x)
srd.plotspec(yhp,Ts)  # Doesn't look quite right?