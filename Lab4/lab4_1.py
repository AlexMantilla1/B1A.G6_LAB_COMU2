
import numpy as np
import math
from matplotlib import pyplot


N = 100
k = 5
n = np.linspace(0,N-1,N)
signal = np.cos(2.*math.pi*k*n/N)
fourier = np.fft.fft(signal)
fourier_mejor = np.fft.fftshift(fourier)

pyplot.plot(n,np.absolute(fourier_mejor))
#pyplot.show()

signal2 = np.exp(1.j*2.*math.pi*k*n/N)
fourier2 = np.fft.fft(signal2)
fourier_mejor2 = np.fft.fftshift(fourier2)

pyplot.plot(n,np.absolute(fourier_mejor2))
pyplot.show()