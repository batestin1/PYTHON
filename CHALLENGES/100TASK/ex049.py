# faça uma tabuada utilizando o comando FOR

print('-*-'*30)
print('TABUADA')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num * c))