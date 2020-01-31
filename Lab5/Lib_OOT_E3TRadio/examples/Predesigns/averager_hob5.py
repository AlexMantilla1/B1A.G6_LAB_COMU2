import numpy
class promediador:
    """
Promedia vectores. a medida que recibe un nuevo vector, entrega otro vector en el que se actualiza el promedio de todos los vectores recibidos hasta el momento.
N: es el tamano del vector
Ensayos: es el numero maximo de veces a promediar. Cuando el numero de vectores que ha recibido este bloque alcanza este numero, se detiene el contador de vectoresn para evitar un overflow y el promediado continua basado en el ultimo valor del contador.
    """
    def __init__(self, N, Ensayos):

# variables que pasan al constructor del Modulo OOT
        self.N=N
        self.Ensayos=Ensayos
        self.med=numpy.empty(N)
        self.count=0    

    def work(self, input_items, output_items):
        in0 = input_items
        out = output_items

        # Inicio de la esencia del codigo que pasa a la funcion work del Modulo OOT
        if self.count < self.Ensayos:
            self.count += 1	
        for i in range(0,self.N):
            self.med[i] = self.med[i]*(self.count-1)/self.count+in0[i]/self.count
        out[:]=self.med
        # Fin de la esencia del codigo que pasa a la funcion work del Modulo OOT
        
        return len(output_items)

# Prueba para comprobar si todo funciona bien.

NN=5
nn=10
y= numpy.empty(NN)

mipro=promediador(5,10)

x=[4.0,2.0,3.0,4.0,5.0]
mipro.work(x,y)
print(y)

x=[8.0,4.0,7.0,1.0,9.0]
mipro.work(x,y)
print(y)


x=[0.0,5.0,12.0,4.0,1.0]
mipro.work(x,y)
print(y)

x=[-2.0,2.0,4.0,4.0,3.0]
mipro.work(x,y)
print(y)

x=[-25.0,6.0,3.0,4.0,8.0]
mipro.work(x,y)
print(y)

