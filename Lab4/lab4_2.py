
import numpy as np
import math
from matplotlib import pyplot
fs = 30
k = 5
t = np.arange(0,4,1/fs)
N = len(t)
print(N)
n = np.arange(0,N,1)

w = np.arange(-math.pi,math.pi,(2*math.pi/N))
#w = np.array([w,math.pi])
f = w*fs/(2*math.pi)
#señal solenoidal
signal = np.cos(2.*math.pi*k*n/N)
fourier = np.fft.fft(signal)
fourier_mejor = np.fft.fftshift(fourier)
fourier_mejor_magnitud = np.absolute(fourier_mejor)
fourier_mejor_magnitud_cuadrado = np.power(fourier_mejor_magnitud, 2)
pyplot.plot(f,fourier_mejor_magnitud_cuadrado)

#señal exp compleja
signal2 = np.exp(1.j*2.*math.pi*k*n/N)
fourier2 = np.fft.fft(signal2)
fourier_mejor2 = np.fft.fftshift(fourier2)
fourier_mejor_magnitud2 = np.absolute(fourier_mejor2)
fourier_mejor_magnitud_cuadrado2 = np.power(fourier_mejor_magnitud2, 2)
pyplot.plot(f,fourier_mejor_magnitud_cuadrado2)

#Mostrar grafica
pyplot.show()


