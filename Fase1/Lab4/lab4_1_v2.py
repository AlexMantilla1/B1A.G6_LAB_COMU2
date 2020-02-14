
import numpy as np
import math
from matplotlib import pyplot as plt
# Parametros de la senal de interes
fo = 1000. # es una frecuencia fundamental
k = 4
f = k*fo # es la frecuencia de la senoidal
N = 32
# Las senales discretas
n = np.linspace(0,N-1,N)
signal = np.cos(2.*math.pi*k*n/N)
signal2 = np.exp(1.j*2.*math.pi*k*n/N)
fourier = np.fft.fft(signal)
fourier2 = np.fft.fft(signal2)
fourier_mejor = np.fft.fftshift(fourier)
fourier_mejor2 = np.fft.fftshift(fourier2)
# calculos para relacional la senal discreta con el mundo real
T = 1./fo
Tsamp = T/N
Fsamp = 1./Tsamp
Fmin = -Fsamp/2.
Fresol = Fsamp/N
Fmax = -Fmin-Fresol
f = np.linspace(Fmin,Fmax,N)
#plt.stem(n,signal)
plt.stem(f,fourier_mejor)  # plt.plot(f,fourier_mejor)
plt.stem(f,fourier_mejor2, linefmt = 'red')  # plt.plot(f,fourier_mejor)
plt.show()




print("Tsamp es: ", Tsamp)
print("Fsamp es: ", Fsamp)
print("Fmin es: ", Fmin)
print("Fresol es: ", Fresol)
print("Fmax es: ", Fmax)