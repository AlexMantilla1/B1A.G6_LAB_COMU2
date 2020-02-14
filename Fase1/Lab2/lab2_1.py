
import numpy as np

def sumar(x,y):
    return x + y

def restar(x,y):
    return x - y

x = np.array([1,2,3,4,5,6])
y = np.array([7,8,9,10,11,12])
print("x es: " , x)
print("y es: " , y)
suma = sumar(x,y)
print("suma (x + y) es: " , suma , "\n")
resta = restar(x,y)
print("suma (x - y) es: " , resta , "\n")
