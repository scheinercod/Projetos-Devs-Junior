#calculadora no python

import numbers
from tokenize import Number
from unicodedata import numeric


while True:
    print()
    n1 = input('Digite 1 numero:')
    n2 = input('Digite proximo Numero:')
    operador = input('Digite um operador logico [Soma [+]. Subtração [-], Multiplicação [*], Divisão [/] ]') 


    if not n1.isnumeric() or not n2.isnumeric():
        print('Favor digitar somente numeros!')
        continue

    n1 = int(n1)
    n2 = int(n2)       
   
    # + - / *

    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '*':
        print(n1 * n2)
    elif operador == '/':
        print(n1 / n2)
    else:
        print('Operador Invalido')