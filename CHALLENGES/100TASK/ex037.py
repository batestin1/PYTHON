#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será
#a base de conversão:

print('-*-'*30)
print('CONVERSOR DE BASES NÚMERICAS ')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

num = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')