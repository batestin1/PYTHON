#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

import random

print('-*-'*30)
print('PAR OU IMPAR')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

n = int(input('Digite um número: '))
res = n % 2
if res == 0:
    print(f'O número {n} é PAR!')
else:
    print(f"O número {n} é IMPAR")