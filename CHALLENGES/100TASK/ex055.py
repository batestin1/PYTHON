#Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

print('-*-'*30)
print('maior e menor sequencia')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {} kg.'.format(maior))
print('O menor peso lido foi de {} kg.'.format(menor))