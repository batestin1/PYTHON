'''

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

import math

from cabecalho import Cabecalho
titulo = Cabecalho('008', 'ESTRUTURA SEQUENCIAL')
print(titulo.texto)

h = float( input( "Quanto você ganha por hora: " ) )
t = float( input( "Quantas horas por dia você trabalha: " ) )
def salario(h,t):

    semana = t * 5
    mes = semana * 4
    total = mes * h
    return print( f"o seu salario no mes é de R${total:.2f}" )

salario(h,t)
