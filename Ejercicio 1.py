"""
Nombre: Hola Mundo.py
Autor: Carbajal Ramos Juan Jesús
Fecha: 04/07/19
"""

#Realice un programa en Python que dado como dato el sueldo de un trabajador,
#le aplique un aumento del 15% si su sueldo es inferior a $1000.00 y del 12% en caso contrario.
#Imprima el nuevo sueldo del trabajador.

def main():
    st = float(input('Introduce sueldo: '))
    if st < 1000:
        sf = st * .15 + st
    else:
        sf = st * .12 + st
        
    print('El sueldo final es: ', str(sf))
    
if __name__ == '__main__':
    main()