#O mesmo professor do desafio 019
# quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

print('-*-'*30)
print('SORTEANDO UMA ORDEM NA LISTA')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

alunos =[]
qan = int(input('Quantos alunos desejam participar do sorteio: '))
for i in range(qan):
    n = input('Digite o nome do aluno: ').upper()
    alunos.append(n)


print(f"""
A lista original é {alunos},
mas a ordem para apagar o quadro será a seguinte:
{shuffle(alunos)}""")
