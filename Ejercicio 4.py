"""
Autor: Carbajal Ramos Juan Jesús
Fecha: 04/07/19
"""

#Realice un programa en Python que permita capturar en una lista las calificaciones
#de N alumnos y que le permita calcular e imprimir lo siguiente:
#
#   1. El promedio general de los alumnos
#   2. Numero de alumnos aprobados y número de alumnos reprobados (Si el alumno sacó una calificación menor a
#       70 se considera reprobado)
#   3. Porcentaje de alumnos aprobados y reprobados.
#   4. Número de alumnos cueya calificación fue mayor a 80

calificaciones = []

def promedio():
    sum = 0.0
    for i in range(0, len(calificaciones)):
        sum = sum + calificaciones[i]

    prom = sum / len(calificaciones)
    return prom

def aprobado():
    apro = 0
    repro = 0
    ochenta = 0

    for i in range(0, len(calificaciones)):
        if calificaciones[i] >= 70:
            if calificaciones[i] >= 81:
                ochenta = ochenta + 1
            apro = apro + 1
        else:
            repro = repro + 1

    print('Aprobados: ', str(apro))
    print('Reprobados: ', str(repro))

    porapro = apro * 100 / len(calificaciones)
    print('Porcentaje de aprobados: ', porapro)
    
    porrepro = repro * 100 / len(calificaciones)
    print('Porcentaje de reprobados: ', porrepro)

    print('Alumnos con mas de 80:', ochenta)

    

def main():
    ciclo = True
    while ciclo == True:

        cal = float(input('Calificacion: '))
        calificaciones.append(cal)
        otro = input('Ingresar otra calificacion? (s/n): ')
        if otro == 'n':
            ciclo = False

    else:
        print('Prmedio: ', str(promedio()))
        aprobado()
    
if __name__ == '__main__':
    main()