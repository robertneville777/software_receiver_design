"""
Created on Thu Dec  6 22:52:58 2018
Listing 3.2: Plot the spectrum of a noise signal. (Page 42)
"""

import numpy as np
import matplotlib.pyplot as plt

time = 1
Ts = 1/10000
x = np.transpose(np.random.randn(1,int(time/Ts))) # Transpose to match other 
t = np.arange(0,time,Ts)                          # time and frequency dimensions
xf = np.fft.fftshift(np.abs(np.fft.fft(x)))
tf = np.arange(-1/(2*time)*x.size, 1/(2*time)*x.size, 1/(time))

fig = plt.figure()
fig.subplots_adjust(hspace = 0.5)
ax1 = fig.add_subplot(211) # 211 means, 2-by-1 grid, select plot 1
ax1.plot(t,x)
ax1.set_xlabel('Seconds')
ax1.set_ylabel('Amplitude')
ax1.grid(True)
ax2 = fig.add_subplot(212) # 212 means, 2-by-1 grid, select plot 2
ax2.plot(tf, xf)
ax2.set_xlabel('Frequency')
ax2.set_ylabel('Magnitude')
ax2.grid(True)
plt.show()