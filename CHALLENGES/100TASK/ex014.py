#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('-*-'*30)
print('CALCULADORA DE TEMPERATURA')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

cel = float(input('Digite a temperatura em Graus Celsius: '))
fah = (cel * 9/5) + 32
ke = cel + 273.15

option = int(input(""" Qual a conversão deseja realizar:
 [1] Kelvin
 [2] Fahrenheit
 """))

if option == 1:
    print(f'{cel}ºC corresponde a {ke}ºK')
else:
    print(f'{cel}ºC corresponde a {fah}ºF')
