#Faça um programa que mostre na tela uma contagem regressiva para o estouro de
# fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

print('-*-'*30)
print('CONTAGEM REGRESSIVA ')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)


from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BUM! BUM! POOOW!')