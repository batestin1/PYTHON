# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

print('-*-'*30)
print('SORTEANDO UM ALUNO')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)


alunos =[]
qan = int(input('Quantos alunos desejam participar do sorteio: '))
for i in range(qan):
    n = input('Digite o nome do aluno: ').upper()
    alunos.append(n)

print(f"""Os alunos voluntariados foram:
{alunos}.
E o sorteado para apagar o quadro foi {random.choice(alunos)}""")
