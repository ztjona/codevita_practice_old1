# -*- coding: utf-8 -*-
'''
Python 3.7.3
[MSC v.1916 64 bit (AMD64)]
22 / 10 / 2020
@author: z_tjona
Cuando escribí este código, solo dios y yo sabíamos como funcionaba. Ahora solo lo sabe dios.
'I find that I don't understand things unless I try to program them.'
-Donald E. Knuth
'''

import unittest
from unittest.mock import patch, call
import digitPairs

''' Auxiliary test for digit Pairs main script.
################################################### '''


class Auxiliar:
    ''' Clase auxiliar para manejar inputs y prints.
    ############################################### '''

    def __init__(self):
        ''' Constructor
        ############################################### '''
        self.numbers = '234 567 321 345 123 110 767 111'
        self.n = 8

    def inputGen(self):
        ''' Mensajes de consola.
        ############################################### '''
        print('input:', self.n)
        yield self.n

        print('input:', self.numbers)
        yield self.numbers


    def printFn(self, query):
        ''' shield de impresiones
        ############################################### '''
        print('printed:', query)



class Pruebas(unittest.TestCase):
    def test_method_bitScoring(self):
        ''' Test for validating bit scoring calculus.
        Test cases from example
        ############################################### '''
        print('Iniciando pruebas')
        numbers = [234, 567, 321, 345, 123, 110, 767, 111]
        solutions = [58, 12, 40, 76, 40, 11, 19, 18]

        for ith_number, ith_solution in zip(numbers, solutions):
            mySol = digitPairs.calculateBitScore(ith_number)
            print(mySol)
            self.assertEqual(mySol, ith_solution)

    @patch('digitPairs.print', create=True)
    @patch('digitPairs.input', create=True)
    def test_example(self, input_mock, print_mock):
        ''' Test for validate example 1
        ############################################### '''
        resultados = [3]

        decors = Auxiliar()
        printFn = decors.printFn
        inputGen = decors.inputGen
        print_mock.side_effect = printFn
        input_mock.inputGen = inputGen()
        input_mock.side_effect = lambda: next(input_mock.inputGen)
        print('Iniciando pruebas')

        digitPairs.main()

        calls = [call(x) for x in resultados]
        print_mock.assert_has_calls(calls)

