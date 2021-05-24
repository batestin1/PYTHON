#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

print('-*-'*30)
print('VERIFICANDO AS PRIMEIRAS LETRAS DE UM TEXTO')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

cidade = input('Em que cidade você nasceu? ').upper()



if  cidade[:5].upper() == 'SANTA':
    print('A sua cidade começa com a palavra SANTA')
elif cidade[:5].upper() == 'SANTO':
    print('A sua cidade começa com a palavra SANTO')
else:
    print('A sua cidade não começa nem com SANTO, nem com SANTA.')