'''

Faça um Programa que converta metros para centímetros.

'''
from cabecalho import Cabecalho
titulo = Cabecalho('005', 'ESTRUTURA SEQUENCIAL')
print(titulo.texto)


def conversor():
    x = int( input( "Entre com um valor númerico: " ) )
    cm = x*100
    return print(f"""{x}m equivale a {cm}cm""")

def repet():
    resp = input("Deseja repetir a operação: ")[0].upper()
    if resp == 'S':
        conversor()
    else:
        print("Obrigado")


conversor()
repet()
