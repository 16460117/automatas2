"""
Autor: Carbajal Ramos Juan Jesús
Fecha: 04/07/19
"""

#Realice un programa en python que permita almacenar en un diccionario los datos generales de un alumno del ITC.
#Deberá poder imprimir cada uno de éstos datos a través de la clave del 
#diccinario y modificar al menos uno de los datos (ej. número telefónico).

import subprocess as sp

datos = {
    'Nombre' : '',
    'Apellido' : '',
    'FechaNacimiento' : '',
    'LugarNacimiento' : '',
    'Nacionalidad' : ''
}

def imprimir():
    sp.call('clear', shell=True)
    print('Los datos son:\n')

    for clave, valor in datos.items():
        print(clave + ": " + str(valor))

    

def modificar():
    opcion = input('Que desea modificar? ')
    dato = input('Por cual dato? ')
    datos[opcion] = dato


def main():

    nombre = input('Nombre: ')
    datos['Nombre'] = nombre

    apellido = input('Apellido: ')
    datos['Apellido'] = apellido

    fecha = input('Fecha de nacimiento: ')
    datos['FechaNacimiento'] = fecha

    nacimiento = input('Lugar de nacimiento: ')
    datos['LugarNacimiento'] = nacimiento

    nacionalidad = input('Nacionalidad: ')
    datos['Nacionalidad'] = nacionalidad

    ciclo = True
    while ciclo == True:

        imprimir()

        mod = input('Desea modificar algun dato?, (s/n): ')
        if mod == 's':
            modificar()
        else:
            ciclo = False

if __name__ == '__main__':
    main()