#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('-*-'*30)
print('AUMENTO DE SALÁRIO')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

sal = float(input('Qual o seu salário atual? '))
aum = sal + (sal* 15/100)

print(f""" Com um bom desempenho deste mês, o chefe decidiu aumentar seu salario em 15%, então seu salário ficou assim:
Salário Atual = R$ {sal};
Salário Aumentado = R$ {aum}""")
