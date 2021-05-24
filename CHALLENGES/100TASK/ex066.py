#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
#o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
#foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('-*-'*30)
print('VÁRIOS NÚMEROS COM FLAGS')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

soma = cont = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores foi {soma}!')