"""
Listing 3.2: Plot the spectrum of a noise signal. (Page 42)
"""

import numpy as np
import srd as srd

time = 1
Ts = 1/10000
x = np.transpose(np.random.randn(1,int(time/Ts))) # Transpose necessary?
srd.plotspec(x,Ts)