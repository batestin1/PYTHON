#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

print('-*-'*30)
print('COMPARANDO NÚMEROS ')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

n1 = int(input('Primeiro número: '))
n2 = int(input('Segunda número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior!')
elif n2 > n1:
    print('O SEGUNDO valor é maior!')
else:
    print('Os dois valores são IGUAIS!')