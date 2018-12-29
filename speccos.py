#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Listing 3.3: Plot the spectrum of a cosine wave. (Page 45)
"""

import numpy as np
import srd as srd

f = 10
phi = 0
time = 2
Ts = 1/100
t = np.arange(0,time,Ts)
x = np.cos(2*np.pi*f*t + phi)
srd.plotspec(x,Ts)