#Escreva um programa que pergunte a
# quantidade de Km percorridos por um
# carro alugado e a quantidade de dias pelos quais ele foi
# alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('-*-'*30)
print('ALUGUEL DE CARROS')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

car = input('Qual o modelo do seu carro: ')
placa = (input('Qual a placa do seu carro: '))
km = int(input('Quantos km você pecorreu com o carro: '))
dia = int(input('Para quantos dias ele foi alugado: '))
preco = (dia*60) + (km*0.15)

print('-*-'*30)
print(f""" 
~~~~~~~~~~~~~~~~~~~~~~
INFORMAÇÕES IMPORTANTES
~~~~~~~~~~~~~~~~~~~~~~
CARRO: {car}
PLACA: {placa}
KM's RODADOS: {km}
ALUGUEL POR DIA: {dia}
PREÇO TOTAL A PAGAR: R$ {preco}


""")