# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
import pandas as pd

print('-*-'*30)
print('CONVERSOR DE MEDIDAS')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

metros = int(input('Digite um valor em metros: '))

km = metros/1000
cm = metros*100
mm = metros*1000
milhas = metros/1609
jardas = metros*1.094
pe = metros*3.28084
polegada = metros*39.37
milnautico = metros/1852

print('-*-'*30)

option = int(input(""" Qual conversão deseja obter: 
[1] = Quilômetros; 
[2] = Centímetros;
[3] = Milímetros;
[4] = Milha
[5] = Jardas
[6] = Pés
[7] = Polegadas
[8] = Milhas Naúticas
"""))

if option == 1:
    print(f'O valor de {metros}m em quilômetros é de {round(km, 3)}km.')
elif option == 2:
    print(f'O valor de {metros}m em centímetros é de {round(cm)}cm.')
elif option == 3:
    print(f'O valor de {metros} em milímetros é de {round(mm)}mm.')
elif option == 4:
    print(f'O valor de {metros}m em milhas é de {round(milhas,3)}mi.')
elif option == 5:
    print(f'O valor de {metros}m em jardas é de {round(jardas)}yd.')
elif option == 6:
    print(f'O valor de {metros}m em pés de altura é de {round(pe)}ft.')
elif option == 7:
    print(f'O valor de {metros} em polegadas é de {round(polegada)}in.')
elif option == 8:
    print(f'O valor de {metros} em milhas náuticas é de {round(milnautico, 3)}nm.')







