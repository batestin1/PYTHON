'''

Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''

import math

from cabecalho import Cabecalho
titulo = Cabecalho('007', 'ESTRUTURA SEQUENCIAL')
print(titulo.texto)


def area():
    b = float(input("Entre com o valor da base: "))
    al = float(input("Entre com o valor da altura: "))
    ar = b * al
    ar2 = ar * ar
    return print(f""" O seu quadrado {ar2:.2f}m² """)
area()
