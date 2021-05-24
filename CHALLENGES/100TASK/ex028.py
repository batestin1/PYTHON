#Escreva um programa que faça o computador
# "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi
# o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

print('-*-'*30)
print('O JOGO DE ADIVINHAÇÃO')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

print('TENTE ADIVINHAR O QUE ESTOU PENSANDO')


def adivinha():
    n = int(input('ESCOLHA UM NÚMERO ENTRE 0 E 5:  '))

    if n == random.randrange(0, 5, 1) :
        print("PARABÉNS, VOCÊ ACERTOU!")
    else :
        print("VOCÊ ERROU!")
    repet()

def repet():
    option = input("QUER TENTAR DE NOVO? ")[0].upper()

    if option == 'S':
        adivinha()
    else:
        print('OBRIGADO')

adivinha()