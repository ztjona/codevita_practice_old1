# -*- coding: utf-8 -*-
#Daniel Diaz

#evito simbolos extranios en los comentarios

''' V3:
*Founded the pattern:
More info at:
https://github.com/ztjona/codevita_practice/wiki

The sequence is described at:
https://oeis.org/A049834
################################################### '''


from collections import defaultdict


f_x = defaultdict(lambda: 0)


def getChocolates(n, k):
    ''' Returns the number of chocolate square pieces that can
    be obtained. It works recursevely updating the variable f_x.
    Assumes width is the max.
    ############################################### '''
    width = max(n, k)
    lenght = min(n, k)
    
    # -----casos base
    if lenght == 0 or width == 0:
       return 0

    # cuando ya se tiene el valor
    if f_x[(width, lenght)] > 0:
        # el valor ya se encontrO, lo retorno,
        # N: ya q solo 1 valor estA registrado, entonces debo ver cuAl de los dos es, hence el max
        return f_x[(width, lenght)]

    # cuando tiene 1 sola columna o 1 sola fila, entonces cada cuadrado es una pieza de chocolate
    if lenght == 1 and width > 1:
        # not even is required to store these values
    #    f_x[(width, lenght)] = width
       return width

    # ------------ Asumo que el valor aun no se encuentra
    # f[a][b] = f[b][a], entonces solo memorizo 1 de los dos valores.
    if width == lenght:
        # es decir q es cuadrado
        # f_x[(width, lenght)] = 1 # tampoco se graba estos valores
        return 1

    else:
        # no es cuadrado
        menor = lenght
        mayor = width

        # f_x[(menor, menor)] = 1  # ya q es un cuadrado

        # encuentro la proporcionalidad
        # i.e. si tengo un cuadrado 11x2, ya sE que lo puedo dividr en 5 de 2x2 y 1 de 1x2
        multiplos = mayor // menor

        if multiplos == 1:
            # solo se puede formar 1 cuadrado de menor-by-menor
            resta = mayor - menor

            #barras de chocolate n x m y m x n dan el mismo resultado
            fSobrante = getChocolates(resta, menor)  # llamada recursiva

            f_x[(width, lenght)] = 1 + fSobrante
            return f_x[(width, lenght)]
        else:
            # se puede formar mAs de un cuadrado
            resta = mayor % menor
            if resta == 0:
                # se forma un nUmero exacto de cuadrados
                fSobrante = 0
            else:
                fSobrante = getChocolates(resta, menor)  # llamada recursiva

            # actualizo todos los valores del mUltiplo
            for i in range(1, multiplos + 1):
                f_x[(menor*i, menor)] = i

            f_x[(width, lenght)] = f_x[(multiplos*menor, menor)] + fSobrante

            return f_x[(width, lenght)]



# def proc(length, width):
#     ''' Asumo al mInimo como fijo
#     ############################################### '''
#     maxV = max(length, width)
#     minV = min(length, width)
    
#     if minV == 1:
#         return maxV
    
#     multiplos = maxV // minV
    
#     residuo = maxV % minV
#     if residuo == 0:
#         return multiplos
#     else:
#         return getChocolates(minV, residuo) + multiplos

# def proc(n, k):
#     a = n
#     b = k
#     r = 1
#     s = 0
#     while r > 0:
#         q = a // b
#         r = a - b*q
#         s = s + q
#         a = b
#         b = r
#         # print(s)
#     return s

def main():
    ''' 
    ############################################### '''
    #programacion dinamica
    longitud_min = int(input())
    longitud_max = int(input())
    ancho_min = int(input())
    ancho_max = int(input())

    suma_total = 0

    deltaAncho = ancho_max - ancho_min + 1
    base = ancho_min
    for length in range(longitud_min, longitud_max + 1):

        if ancho_min > 1 or length > 1:
            multiplos = ancho_min // length 
            base = ancho_min % length

            suma_total += multiplos* deltaAncho
        else:
            base = ancho_min
        
        for width in range(base, base + deltaAncho):
            # a = proc(length, width)
            a = getChocolates(length, width)

            # a = getChocolates(length, width)
            # print(a)
            suma_total += a

    print(suma_total)

    return


if __name__ == "__main__":
    main()
