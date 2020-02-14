
import numpy as np
import math
from matplotlib import pyplot as plt
#Parametros de la senal analiada
f = 3540.
Fsamp = 9000. # la frecuencia de muestreo
# La senal discreta
N = 128
n = np.linspace(0,N-1,N)
t = n/Fsamp
signal = np.cos(2.*math.pi*f*t)
fourier = np.fft.fft(signal)
fourier_mejor = np.fft.fftshift(fourier)
# Calculo la fft al cuadrado
fourier_cuadrado = np.power(fourier_mejor,2)
# Calculos para relacional la senal discreta con el mundo real
Fmin = -Fsamp/2.
Fresol = Fsamp/N
Fmax = -Fmin-Fresol
f = np.linspace(Fmin,Fmax,N)
# Grafica
plt.stem(f,np.absolute(fourier_cuadrado))
plt.title('|signal(f)| ^ 2')
plt.xlabel('Frequency [Hz]')
plt.show()
