#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).

import time

print('-*-'*30)
print('ANALISADOR DE TEXTO')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

nome = input('Digite o seu nome completo: ')
print('-*-'*30)
print('ANALISANDO...')
time.sleep(1)
print(f"""
Seu nome em maiúsculo é {nome.upper()}
Seu nome em minisculo é {nome.lower()}
O total de letras de seu nome è {len(nome) - nome.count(' ')}
O seu primeiro nome tem {nome.find(" ")} letras,


""")

