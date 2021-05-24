'''

Faça um Programa que peça dois números e imprima a soma.
'''

from cabecalho import Cabecalho

titulo = Cabecalho('003', 'ESTRUTURA SEQUENCIAL')
print(titulo.texto)

def soma():
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite um outro número: '))
    sum = num1 + num2
    return print(f'A soma entre {num1} + {num2} é = {sum}')

def repet():
    resp = input('Deseja repetir a operação? ')[0].upper()
    if resp == 'S':
        soma()
    else:
        print('Obrigado por ter participado do programa!')

soma()
repet()





