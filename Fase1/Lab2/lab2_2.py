
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

calc = Calculadora()
x = np.array([1,2,3,4,5,6])
y = np.array([7,8,9,10,11,12])
print("x es: " , x)
print("y es: " , y)
suma = calc.sumar(x,y)
print("suma (x + y) es: " , suma , "\n")
resta = calc.restar(x,y)
print("resta (x - y) es: " , resta , "\n")
mult = calc.multiplicar(x,y)
print("mult (x * y) es: " , mult , "\n")
divi = calc.dividir(x,y)
print("divi (x / y) es: " , divi , "\n")

