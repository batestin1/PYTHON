#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

print('-*-'*30)
print('DESCONTO DE 5%')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

prod = float(input('Qual o valor do seu produto: '))
desc = prod - (prod * 5/100)

print(f'O seu produto custa R$ {prod} e com desconto de 5% ele passa a valer R$: {desc}.')