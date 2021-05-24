#Faça um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.


print('-*-'*30)
print('HIPOTENUSA')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hip = (co ** 2 + ca ** 2) ** (0.5)
print(f'A hipotenusa vai medir {hip:.2f}º')