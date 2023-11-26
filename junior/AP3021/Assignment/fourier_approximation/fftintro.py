# %%
# -*- coding: utf-8 -*-
"""FFTintro.ipynb

Original file is located at
    https://colab.research.google.com/drive/1_joFdxLAoU7DtxLCDEY7EJRTfO_E9dhh

# FFT Introduction
Using scipy.fft
https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html

給定一矩陣x (t space)，對其進行FFT，產生y矩陣 (s space)
"""

import numpy as np
from scipy.fft import fft, ifft
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
yinv = ifft(y)
print(y)
print(yinv)
print(np.sum(x))
"""### Example of the FFT of the sum of two sines

將兩個波疊加，使用FFT分析

"""

import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

# Number of sample points
N = 600

# sample spacing
T = 1.0 / 800.0  #給定週期
x = np.linspace(0.0, N * T, N, endpoint=False)
y = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)  #兩個波
yf = fft(y)  #轉換
xf = fftfreq(N, T)[:N // 2]  #頻率

plt.figure(2)  #波譜分析(s space)
plt.plot(xf, 2.0 / N * np.abs(yf[0:N // 2]))
plt.grid()

plt.figure(1)  #真實值(t space)
plt.plot(x, y)

plt.show()
# %%
