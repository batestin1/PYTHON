'''

Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
          como parâmetro e mostre uma mensagem com o tamanho adaptável
'''

print('-*-'*30)
print('UM PRINT ESPECIAL ')
print('Desenvolvido por Maycon Cypriano')
print('-*-'*30)

def escreva(mensagem):
    print('-' * (len(mensagem) + 4))
    print(f'  {mensagem}  ')
    print('-' * (len(mensagem) + 4))


escreva('Olá, mundo')
escreva('Python é a melhor linguagem do mundo')
escreva('Python é maior que Java')