#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.


import math


print('-*-'*30)
print('SENO, COSSENO E TANGENTE')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

ang = float(input("Qual a medida de seu Ângulo: "))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print(f""" Eis os resultados obtidos: 
SENO: O SENO de {ang}º é {sen:.2f}º;
COSSENO: O COSSENO de {ang}º é {cos:.2f}º;
TANGENTE: A TANGENTE de {ang}º é {tang:.2f}º.
""")