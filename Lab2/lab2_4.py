
import numpy as np

class Calculadora:
    def __init__(self):
        print ("Se creo una calculadora")
    def sumar(self,x,y):
        return x + y
    def restar(self,x,y):
        return x - y
    def multiplicar(self,x,y):
        return x*y
    def dividir(self,x,y):
        return x/y

class CalcAleatorea(Calculadora):
    def __init__(self):
        Calculadora.__init__(self)
    def media(self,x):
        return (np.sum(x))/len(x)
    def mediaCuadratica(self,x):
        z = np.power(x,2)
        return (np.sum(z))/len(z)
    def varianza(self,x):
        media = self.media(x)
        return self.mediaCuadratica(x-media)
    def desviacionEstandar(self,x):
        return np.sqrt(self.varianza(x))
    def correlacion(self,x,y):
        return self.media(x*y)

calc2 = CalcAleatorea()
t = np.linspace(0,20,2000000)
y = np.exp(-0.5*t)
media = calc2.media(y)
print("media de y es: " , media)

