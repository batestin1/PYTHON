#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

import random

print('-*-'*30)
print('RADAR ELETRÔNICO')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

vel = float(input("Qual é a velocidade do carro: "))
multa = (vel - 80) * 7

if vel > 80:
    print(f"""MULTADO!!!
Você excedeu o limite permitido que é de 80Km/h, e sua multa será de R${multa}""")
else:
    print(""" DENTRO DA NORMA!!!
Você está dirigindo de modo seguro! Tenha um bom dia!""")
