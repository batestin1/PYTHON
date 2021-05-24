#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
import pandas

print('-*-'*30)
print('CONVERSAO DE DOLAR ')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

real = float(input('Quanto você tem na carteira: '))
dolar = real*0.18
print(f'Se você tem R$:{real} na carteira, então você tem USD:{round(dolar,2)}')