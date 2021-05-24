# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

print('-*-'*30)
print('CUSTO DA VIAGEM')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

dist = float(input("Qual é a distância da viagem?  "))
preco = dist * 0.50 if dist <= 200 else dist * 0.45
print(f"E o preço da sua passagem será de R${preco:.2f}")