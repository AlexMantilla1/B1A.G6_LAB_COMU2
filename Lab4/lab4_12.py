


import numpy as np
import math
from matplotlib import pyplot
#N = 100
fs = 20
k = 5
t = np.arange(0,4,1/fs)
N = len(t)
print(N)
n = np.arange(0,N,1)
signal = np.cos(2.*math.pi*k*n/N)
fourier = np.fft.fft(signal)
fourier_mejor = np.fft.fftshift(fourier)
pyplot.plot(n,np.absolute(fourier_mejor))
#pyplot.show()
signal2 = np.exp(1.j*2.*math.pi*k*n/N)
fourier2 = np.fft.fft(signal2)
fourier_mejor2 = np.fft.fftshift(fourier2)
pyplot.plot(n,np.absolute(fourier_mejor2))
#pyplot.plot(t,signal)
pyplot.show()