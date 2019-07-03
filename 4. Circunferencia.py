"""
Nombre: Circunferencia.py
Objetivo: Calcula el area y diametro de un circulo
Autor: Carbajal Ramos Juan Jesús
Fecha: 01/07/19
"""

#   Libreria matematica
import math
#   Libreria para limpiar pantalla
import subprocess as sp

#----------------------------------------------------------
#   Funcion para calcular
#----------------------------------------------------------
def calculaArea(r):
    area = math.pi*(math.pow(r, 2))
    return area

def calculaDiametro(r):
    diametro = r * 2
    return diametro

#----------------------------------------------------------
#   Funcion principal
#----------------------------------------------------------
def main():
    
    ciclo = True
    while ciclo == True:

        sp.call('clear', shell=True)
        print('-- Script para calcular el Area de circulo')
        radio = float(input('\nIntroduce el valor del radio: '))

        #   Invoca los metodos
        print('\nEl area es: ', str(calculaArea(radio)))
        print('El diametro es: ', str(calculaDiametro(radio)))

        r = input('\nOtro calculo (s/n)? ')
        if r == 'n' or r == 'N':
            ciclo = False


if __name__ == '__main__':
    main()