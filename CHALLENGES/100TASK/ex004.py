#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

print('-*-'*30)
print('DISSECANDO UMA VARIÁVEL')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

v = input('Digite algo: ')
print('-*-'*30)
option = int(input(f""" A respeito de sua expressão {v}, quais das informações abaixo deseja conhecer? 

[1] - TIPO PRIMITIVO
[2] - POSSUÍ ESPAÇO
[3] - É NÚMERICO 
[4] - É ALFABÉTICO
[5] - É ALFANÚMERICO
[6] - MAIÚSCULA
[7] = MINÚSCULO
[8] = ESTÁ CAPITALIZADO 
   """))

if option == 1:
    print(type(v))
elif option == 2:
    print(v.isspace())
elif option == 3:
    print(v.isnumeric())
elif option == 4:
    print(v.isalpha())
elif option == 5:
    print(v.isalnum())
elif option == 6:
    print(v.isupper())
elif option == 7:
    print(v.islower())
elif option == 8:
    print(v.istitle())



