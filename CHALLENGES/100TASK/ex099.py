'''

Faça um programa que tenha a função maior(), que recebe vários parâmetros
          com valores inteiros.
          Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

print('-*-'*30)
print('FUNÇÃO DESCOBRE O MAIOR NÚMERO')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

from time import sleep


# Função para impressão de barra
def barra():
    print('-' * 50)


# Função para verificar o maior valor entre vários informados
def maior(*args):
    barra()
    print('Os valores estão em processo de análise...')
    sleep(1.5)

    # Percorrendo tupla de valores
    maior = None
    for elemento in args:

        print(elemento, end=' ')
        sleep(0.5)
        if maior is None or elemento > maior:
            maior = elemento

    print(f'--> {len(args)} Valores informados...')
    print(f'O maior valor é --> {maior}')



maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()