'''

Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
'''

from cabecalho import Cabecalho

titulo = Cabecalho('002', 'ESTRUTURA SEQUENCIAL')
print(titulo.texto)


def title(y):
    print(f"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~ EXERCICIO {y} - ESTRUTURAL SEQUENCIAL ~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~ DESENVOLVIDO POR MAYCON CYPRIANO ~~~~~~~~~~~~~~~~~~~~~~~
""")

title('002')

def num(x):
    print(f'O numero informado foi {x}')

x = int(input('Digite um número: '))

num(x)