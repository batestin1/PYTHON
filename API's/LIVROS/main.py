# este é um projeto de extração e transformação de dados da api de livros
# link da api https://www.googleapis.com/

import requests
import random
from book import Livros
from typewriter import MaquinadeEscrever



def main():
    global texto
    global nome
    global titulo
    global autor
    global sinopse
    print('#'*100)
    print('')
    texto = 'Digite abaixo o nome do livro que deseja consultar:'
    MaquinadeEscrever(texto).mensagem
    print('')
    print('#' * 100)
    print('')
    nome = input('')
    print('')
    titulo = Livros(nome).titulo
    autor = Livros(nome).autor
    sinopse = Livros(nome).sinopse
    print('#' * 100)
    print('')
    textoFinal = f"""
    Titulo Oficial = {titulo},
    Autor(a) = {autor},
    Sinopse = {sinopse}
    """
    MaquinadeEscrever(textoFinal).mensagem
    print('#' * 100)

if __name__== '__main__':
    main()