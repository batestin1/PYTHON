#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

print('-*-'*30)
print('PROCURANDO UMA STRING DENTRO DE OUTRA')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

nome = input('Digite o seu nome completo: ').upper()

if 'SILVA' in nome.upper():
    print('Parabéns! Seu nome tem SILVA no meio.')
else:
    print('Seu nome não tem SILVA em lugar algum')