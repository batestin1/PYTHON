#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

print('-*-'*30)
print('PRIMEIRO E ÚLTIMO NOME DA PESSOA')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

nome = input('Digite o seu nome completo: ')
nome = nome.split()
first = nome[0]
last = nome[len(nome)-1]
meio = nome[len(nome)-2]
print(f"""
PRIMEIRO NOME: {first}
ÚLTIMO NOME: {last}
NOME DO MEIO: {meio}""")