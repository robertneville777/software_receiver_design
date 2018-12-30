"""
Listing 3.5: Change the frequency of the input. (Page 54)
"""

import numpy as np
import srd as srd

time = 0.5
Ts = 1/10000
t = np.arange(0,time,Ts)
fc = 1000
cmod = np.cos(2*np.pi*fc*t)
fi = 100
x = np.cos(2*np.pi*fi*t)
y = cmod*x
srd.plotspec(cmod, Ts)
srd.plotspec(x, Ts)
srd.plotspec(y, Ts)