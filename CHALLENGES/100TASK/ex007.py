#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('-*-'*30)
print('MÉDIA ARITIMÉTICA')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

aluno1 = input('Digite o nome do aluno: ')
nota1 = int(input(f'Qual a nota de português do {aluno1}: '))
nota2 = int(input(f'Qual a nota de matemática do {aluno1}: '))
nota3 = int(input(f'Qual a nota de ciências do {aluno1}: '))
nota4 = int(input(f'Qual a nota de educação física do {aluno1}: '))
media = (nota1+nota2+nota3+nota4) / 4
print('-*-'*30)
print(f'A media de todas as notas de {aluno1} é de {media} pontos')
