"""
Nombre: Operaciones.py
Objetivo: Realizar operaciones basicas con 2 numeros, comparar los numeros y contar con esos numeros
Autor: Carbajal Ramos Juan Jesús
Fecha: 29/06/19
"""

# Fincion para sumar
def suma(num1, num2):
    return num1 + num2

# Fincion para restar
def resta(num1, num2):
    return num1 - num2

# Fincion para miltiplicar
def mult(num1, num2):
    return num1 * num2

# Fincion para dividir
def divi(num1, num2):
    return num1 / num2

# Funcion para comparar
def compara(num1, num2):
    if (num1 > num2):
        print('El mayor es num1:', num1)
    elif (num1 < num2):
        print('El mayor es num2:', num2)
    else:
        print('Num1 y num2 son iguales', num1, ',', num2)

# Funcion para contar de num1 a num2
def cuenta(num1, num2):
    for i in range(num1, num2 + 1):
        print('valor de i:', i)

# Funcion principal
def main():
    ciclo = True
    while(ciclo == True):

        n1 = int(input('Primer numero: '))
        n2 = int(input('Segundo numero: '))

        # Operaciones basicas
        print('\nLa suma es: ' + str(suma(n1, n2)))
        print('La resta es: ' + str(resta(n1, n2)))
        print('La multipliacion es: ' + str(mult(n1, n2)))
        print('La divicion es: ' + str(divi(n1, n2)))

        # Llamada a las funciones compara y cuenta
        compara(n1, n2)
        cuenta(n1, n2)
        
        # Decidir si se desea realizar mas operaciones
        cad = input('\nOtro calculo (s/n)? ')
        if (cad == 's' or cad == 'S'):
            ciclo = True
        else:
            ciclo = False

if __name__ == '__main__':
    main()