"""
Nombre: Factorial.py
Objetivo: Calcular el factorial de un numero
Autor: Carbajal Ramos Juan Jesús
Fecha: 01/07/19
"""

# Metodo recursivo
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

# Funcion principal
def main():
	num = int(input('Numero: '))
	print('El factorial es: ', str(factorial(num)))

if __name__ == '__main__':
	main()
