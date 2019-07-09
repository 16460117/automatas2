
"""
Autor: Carbajal Ramos Juan Jesús, Mancilla tinoco Mario Ruben y Montoro Sandoval Maria Fernanda
Fecha: 04/07/19
"""

#script para analizar lexicamente la sentencia printf en Ansi c

def lexico(c):
    printf = c.find('printf')
    if printf == 0:
        parI = c.find('(')
        if parI == 6 or parI == 7:
            comI = c.find('\'')
            if comI == 7 or comI == 8:
                parF = c.find(')')
                if parF == -1:
                    print('Falta \')\'')
                else:
                    parF = parF - 1
                    if c[parF] == '\'':
                        comI = comI + 1
                        mensaje = c[comI:parF]
                        pyc = c.find(';')
                        if len(c) - 1 == pyc:
                            print('printf: Inicio de sentencia')
                            print('(: PArentesis de apertura')
                            print('\': Comilla de apertura')
                            print(mensaje, ': Mensaje')
                            print('\': Comilla de cierre')
                            print('): Parentesis de cierre')
                            print(';: Fin de sentencia')
                        else:
                            print('falta ;')
                        
                    else:
                        print('Falta \'\'\' de cierre')
            else:
                print('Falta \'\'\' de apertura')
        else:
            print('Falta \'(\'')
    else:
        print(printf)
        print('Falta printf')

def main():
    print('-- Analisis lexico de la sentencia printfn --')
    cadena = input('Cadena: ')
    lexico(cadena)

if __name__ == '__main__':
    main()
