# Escreva um programa que leia um número n inteiro qualquer e mostre na telas os n primeiros elementos de uma sequência Fibonacci.

print('-*-'*30)
print('SEQUÊNCIA DE FIBONACCI')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)
n = int(input('Quantos termos você quer mostrar?'))

n1 = 0
n2 = 2
print('-*-'*30)
print(f'{n1} -> {n2} ->', end='')
cont = 3

while cont <= n:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont +=1
    print(f' {n3} -> ', end='')

print('FIM')