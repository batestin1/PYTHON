#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

print('-*-'*30)
print('ANO BISSEXTO')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))