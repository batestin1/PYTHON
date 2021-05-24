#Faça um programa que leia uma
# frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

print('-*-'*30)
print('PROCURANDO UMA STRING DENTRO DE OUTRA')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

frase = input('Digite uma frase qualquer: ').upper()

quant = frase.count('A')
first = frase.find('A')+1
last = frase.rfind('A')+1

print(f"""A letra 'A' aparece {quant} vezes na frase {frase}
A primeira vez que ela ocorre está na posição {first}
A ultima ocorrência está na posição {last}""")
