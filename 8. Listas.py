"""
Nombre: Listas.py
Objetivo: Hacer un GRUD con listas
Autor: Carbajal Ramos Juan Jesús
Fecha: 2/07/19
"""

#Importa la libreria para limipar la consola de ubuntu
import subprocess as sp

#Declara la lista
lista = []

#Metodo para parar la ejecucion del programa
def parar():
	paro = input('')

#Metodo para agregar un dato a la lista
def agregar(d):
	lista.append(d)

#Metodo para buscar un dato en la lista y muesta su posicion
def buscar(d):
	if d in lista:
		print('El dato esta en la posicion: ', str(lista.index(d)))
	else:
		print('Dato no encontrado')
	parar()

#Metodo para eliminar un dato de la lista
def eliminar(d):
	if d in lista:
		lista.remove(d)
		print('Dato eliminado')
	else:
		print('Dato no encontrado')
	parar()

#Metodo para imprimir todos los datos de la lista
def imprimir():
	j = 0
	for i in lista:
		print('Dato: ', j, ',', i)
		j = j +1
	parar()

#Metodo principal
def main():
	
	ciclo = True
	while ciclo == True:

		sp.call('clear', shell=True)
		print('--- Script para trabajar con listas ---\n')
		print('0. Salir')
		print('1. Agregar')
		print('2. Buscar')
		print('3. Eliminar')
		print('4. imprimir\n')

		opcion = int(input('Opcion: '))

		if opcion == 0:
			ciclo = False
		elif opcion == 1:
			dato = input('\nDato: ')
			agregar(dato)
		elif opcion == 2:
			dato = input('\nDato: ')
			buscar(dato)
		elif opcion == 3:
			dato = input('\nDato: ')
			eliminar(dato)
		elif opcion == 4:
			imprimir()
		else:
			print('ERROR: Opcion no valida')
			parar()
			

			
if __name__ == '__main__':
	main()
