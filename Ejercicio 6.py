"""
Autor: Carbajal Ramos Juan Jesús
Fecha: 05/07/19
"""

import math

class Punto(object):
    def __init__(self, x, y):
         self.x = x
         self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def toString(self):
        return 'El punto tiene las siguientes coordenadas', self.x, ',', self.y

class Circunferencia(Punto):

    def __init__(self, radio):
        self.radio = radio
    
    def getRadio(self):
        return self.radio

    def setRadio(self, radio):
        self.radio = radio

    def getArea(self):
        return math.pi * math.pow(self.getRadio(), 2)

    def toString(self):
        return 'La circunferencia tiene como centro:', self.getX(), ',', self.getY(), ',', self.getRadio(), 'el area es: ', self.getArea()

class Cilindro(Circunferencia):

    def __init__(self, altura):
        self.altura = altura

    def getAltura(self):
        return self.altura
    
    def setAltura(self, altura):
        self.altura = altura

    def getVolumen(self):
        return self.getArea() * self.altura

    def toString(self):
        return 'El volumen es:', self.getVolumen()


def main():

    p1 = Punto(2,3)
    print(p1.toString())

    p2 = Punto(0,0)
    print(p2.toString())

    p2.setX(-2)
    p2.setY(-4)
    print(p2.toString())

    p3 = Circunferencia(12.34)
    p3.setX(10)
    p3.setY(12)
    print(p3.toString())

    p4 = Cilindro(9.81)
    p4.setRadio(3.12)
    p4.setX(2)
    p4.setY(2)
    print(p4.toString())

if __name__ == '__main__':
    main()
