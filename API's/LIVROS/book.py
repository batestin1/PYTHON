#construindo a api

import requests
import pandas as pd
from pymongo import MongoClient

#conexao
client = MongoClient('localhost', 27017)

class Livros():
    def __init__(self, nome):
        self.nome = ''
        self.dados = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={nome}').json()
        self.titulo = self.dados['items'][0]['volumeInfo']['title']
        self.autor = self.dados['items'][0]['volumeInfo']['authors'][0]
        self.sinopse = self.dados['items'][0]['volumeInfo']['description']
        self.livro = {'NOME DO LIVRO': [self.titulo],
                       'NOME DO AUTOR': [self.autor],
                   'SINOPSE': [self.sinopse]}
        self.livro = pd.DataFrame(self.livro)
        db = client['BIBLIOTECA']
        collections = db['LIVRO']
        collections.insert_many(self.livro.to_dict('Results'))
