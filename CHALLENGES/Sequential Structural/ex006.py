'''
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área
'''

import math

from cabecalho import Cabecalho
titulo = Cabecalho('006', 'ESTRUTURA SEQUENCIAL')
print(titulo.texto)

def area():
    r = float(input("Entre com o valor do raio: "))
    a = math.pi * (r*r)
    return print(f"""Para o raio de um círculo no valor de {r}r, sua área é de {a:.2f}º""")

area()

