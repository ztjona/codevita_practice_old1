# -*- coding: utf-8 -*-
'''
Python 3.8.6
[MSC v.1916 64 bit (AMD64)]
29 / 11 / 2020
@author: z_tjona
"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
'''
from fractions import Fraction
from math import ceil, factorial

''' 

################################################### '''

# creating combs dic
combs = dict()
factorialDict = dict()


def factorials(x):
    ''' 
    
    ############################################### '''
    if x not in factorialDict:
        factorialDict[x] = factorial(x)
    return factorialDict[x]


def nchoosek(n, k):
    ''' 
    
    ############################################### '''
    if (n, k) not in combs:
        combs[(n, k)] = factorials(n) // (factorials(k)*factorials(n - k))

    return combs[(n, k)]


def main():
    ''' 
    
    ############################################### '''
    T = int(input())

    for _ in range(T):
        A, H, L1, L2, M, C = map(int, input().split())

        constAtack = A*M
        # faltante, to be with luck
        remainingH = H - constAtack

        if remainingH < 0:
            # de ley pero de ley
            print('1/1')
            continue

        # still alive
        if remainingH > C*M:
            # too strong
            print('RIP')
        else:
            # there is a chance...

            # find the minimum number of seconds that require to run combos
            minCombos = ceil(remainingH/C)
            probNumerator = 0
            for i in range(minCombos, M + 1):
                probNumerator += nchoosek(n=M, k=i) * \
                    (L1**i)*((L2 - L1)**(M - i))

            frac = Fraction(probNumerator, L2**M)
            print(frac.numerator, '/', frac.denominator, sep='')

    return


if __name__ == "__main__":
    main()
