"""
Autor: Carbajal Ramos Juan Jesús
Fecha: 04/07/19
"""

#Realice un programa en Python que dado como datos los sueldos de 10 trabajadores de una empresa,
#obtenga el total de nómina de la misma. Puede utilizar un ciclo for o un ciclo while. 

def main():
    st = 0.0
    for i in range(0, 10):
        print('Sueldo', i + 1, ': ', end = '')
        s = float(input(''))
        st = st + s

    print('Total nominal: ', st)
    
    
if __name__ == '__main__':
    main()