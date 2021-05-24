# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

print('-*-'*30)
print('SEPARANDO DÍGITOS DE UM NÚMERO')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

n = int(input('Digite um número: '))
unidades = n // 1 % 10
dezenas = n // 10 % 10
centenas = n // 100 & 10
milhar = n // 1000 % 10
print(f"""Analisando o número {n}:
UNIDADE: {unidades}
DEZENAS: {dezenas}
CENTENAS: {centenas}
MILHAR: {milhar}""")
