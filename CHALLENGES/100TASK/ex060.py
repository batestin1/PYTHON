#Faça um programa que leia um número qualquer e mostre seu fatorial.

print('-*-'*30)
print('FATORIAL')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)


n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))