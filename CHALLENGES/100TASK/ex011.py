#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print('-*-'*30)
print('PINTANDO A PAREDE ')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

lar = float(input('Digite o valor da largura da parede: '))
alt = float(input('Digite o valor de altura de parede: '))
area = lar*alt
tinta = area/2

print(f'A sua parede tem dimensão {lar} X {alt} e a área é de {area}m², para pinta-la você precisará de {tinta}l de tinta.')


