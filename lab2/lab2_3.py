
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
x = np.array([7,6,10,9,12,14])
y = np.array([7,8,9,10,11,12])
print("x es: " , x)
print("y es: " , y)
media = calc2.media(x)
print("media de x es: " , media)
mediaCua = calc2.mediaCuadratica(x)
print("mediaCua de x es: " , mediaCua)
varianza = calc2.varianza(x)
print("varianza de x es: " , varianza)
devEst = calc2.desviacionEstandar(x)
print("devEst de x es: " , devEst)
corr = calc2.correlacion(x,y)
print("corr de x,y es: " , corr)
