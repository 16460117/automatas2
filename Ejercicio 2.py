"""
Autor: Carbajal Ramos Juan Jesús
Fecha: 04/07/19
"""

#Realice un programa en Python que dado como datos la categoría y el sueldo de un trabajor,
#calcule el aumento correspondiente teniendo en cuenta
#la siguiente información e imprima el nuevo sueldo del trabajador:

def aumento(i):
    if i == 1:
        return 0.15
    elif i == 2:
        return .1
    elif i == 3:
        return 0.08
    elif i == 4:
        return 0.07

def main():
    ss = float(input('Introduce sueldo: '))
    st = int(input('Introduce categoria: '))
    ss = ss * aumento(st) + ss
    print('El sueldo final es: ', str(ss))
    
    
if __name__ == '__main__':
    main()