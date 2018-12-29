"""
Listing 3.1: Plot spectrum of a square wave. (Page 42)
"""

import numpy as np
import srd as srd

f = 10
time = 2
Ts = 1/1000
t = np.arange(0,time,Ts)
x = np.sign(np.cos(2*np.pi*f*t))
srd.plotspec(x,Ts)