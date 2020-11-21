# -*- coding: utf-8 -*-
#Daniel Diaz

#evito simbolos extranios en los comentarios

''' V2:
*Se cambiO la variable f_x de 1 [list][list] a un defaultdict(tuple)
*AdemAs, no se completa toda la matriz desde 1-max(width, length) si no
se completa los pares que se requieren a travEs de llamadas recursivas.
*Cuando se tiene un tamanho 1-c o r-1 se resuelve automAticamente.
################################################### '''

from collections import defaultdict


f_x = defaultdict(lambda: 0)


def getChocolates(width, lenght):
    ''' Returns the number of chocolate square pieces that can
    be obtained. It works recursevely updating the variable f_x.
    ############################################### '''
    # -----casos base
    # cuando ya se tiene el valor
    if (f_x[(width, lenght)] > 0 or f_x[(lenght, width)] > 0):
        # el valor ya se encontrO, lo retorno,
        # N: ya q solo 1 valor estA registrado, entonces debo ver cuAl de los dos es, hence el max
        return max(f_x[(width, lenght)], f_x[(lenght, width)])

    # cuando tiene 1 sola columna o 1 sola fila, entonces cada cuadrado es una pieza de chocolate
    if (width == 1 and lenght > 1) or (lenght == 1 and width > 1):
       f_x[(width, lenght)] = max(width, lenght)

       return f_x[(width, lenght)]

    # ------------ Asumo que el valor aun no se encuentra
    # f[a][b] = f[b][a], entonces solo memorizo 1 de los dos valores.
    if width == lenght:
        # es decir q es cuadrado
        f_x[(width, lenght)] = 1
        return f_x[(width, lenght)]

    else:
        # no es cuadrado
        menor = min(width, lenght)
        mayor = max(width, lenght)

        f_x[(menor, menor)] = 1  # ya q es un cuadrado

        # encuentro la proporcionalidad
        # i.e. si tengo un cuadrado 11x2, ya sE que lo puedo dividr en 5 de 2x2 y 1 de 1x2
        multiplos = mayor // menor

        # solo se puede formar 1 cuadrado de menor-by-menor
        if multiplos == 1:
            resta = mayor - menor

            #barras de chocolate n x m y m x n dan el mismo resultado
            f_x[(resta, menor)] = getChocolates(
                resta, menor)  # llamada recursiva

            f_x[(width, lenght)] = 1 + f_x[(resta, menor)]
            return f_x[(width, lenght)]
        else:
            # se puede formar mAs de un cuadrado

            resta = mayor % menor
            if resta == 0:
                # se forma un nUmero exacto de cuadrados
                fSobrante = 0
            else:
                f_x[(resta, menor)] = getChocolates(
                    resta, menor)  # llamada recursiva
                fSobrante = f_x[(resta, menor)]

            # # actualizo todos los valores del mUltiplo
            # for i in range(1, multiplos + 1):
            #     f_x[(menor*i, menor)] = i

            f_x[(width, lenght)] = f_x[(multiplos*menor, menor)] + fSobrante

            return f_x[(width, lenght)]


def main():
    ''' 
    
    ############################################### '''
    #programacion dinamica
    longitud_min = int(input())
    longitud_max = int(input())
    ancho_min = int(input())
    ancho_max = int(input())

    # creating a matrix with zeros of size mayor-by-mayor
    # cambio la matriz por un diccionario, para no llenar la matriz de gana.
    # f_x = []
    # for _ in range(mayor):
    #     f_x.append([0]*mayor)

    #representa un cuadrado de 1x1
    f_x[(1, 1)] = 1  # ya q tabajo con un diccionario, puedo hacer q se base en 1

    suma_total = 0

    for i in range(longitud_min, longitud_max + 1):
        for j in range(ancho_min, ancho_max + 1):
            a = getChocolates(i, j)
            # print(a)
            suma_total += a

    print(suma_total)

    return


if __name__ == "__main__":
    main()
