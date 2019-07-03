"""
Nombre: Triangulo.py
Objetivo: Deicidir que tipo de triangulo es dado los lados y calcular su perimetro
Autor: Carbajal Ramos Juan Jesús
Fecha: 01/07/19
"""
#   Libreria para borrar consola en linux
import subprocess as sp

# Metodo que compara los lados del triangulo para decidir que tipo de triangulo es
def compara(a, b, c):
    if a == b:
        if a == c:
            tipo = 0
        else:
            tipo = 1
    elif a == c or b == c:
        tipo = 1
    else:
        tipo = 2
    return tipo

#   Metodo para calcular el perimetro
def perimetro(a, b, c):
    perimetro = a + b + c
    return perimetro

#   Metodo principal
def main():

    #   Lista con los tipos de triangulos
    tipos = ['equilatero', 'isosceles', 'escaleno']

    ciclo = True
    while ciclo == True:

        #   Borrador de pantalla
        sp.call('clear', shell=True)

        lado1 = float(input('Lado 1: '))
        lado2 = float(input('Lado 2: '))
        lado3 = float(input('Lado 3: '))

        print('\nEl triangulo es de tipo:', tipos[compara(lado1, lado2, lado3)])
        print('El perimetro del triangulo es:', perimetro(lado1, lado2, lado3))

        #   if para salir o realizar otro calculo
        r = input('\nOtro calculo (s/n)? ')
        if r == 'n' or r == 'N':
            ciclo = False


if __name__ == '__main__':
    main()