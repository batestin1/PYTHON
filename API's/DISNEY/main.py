import requests
import pandas as pd
from pymongo import MongoClient
import pymongo

#working connection
client = MongoClient('localhost', 27017)

def extrac():
    try:
        for i in range(1, 149):
            dados = requests.get(f'https://api.disneyapi.dev/characters?page={i}').json()
            for var in range(0, 49):
                nome = dados['data'][var]['name']
                filme = dados['data'][var]['films'][0]
                shows = dados['data'][var]['tvShows'][0]
                allies = dados['data'][var]['allies'][0]
                enemies = dados['data'][var]['enemies'][0]

                disney = {'Nome': [nome],
                          'Filmes': [filme],
                          'TV Shows(Séries)': [shows],
                          'Aliados': [allies],
                          'Inimigos': [enemies]}

                disney = pd.DataFrame(disney)

                db = client['DISNEY']
                collections = db['PERSONAGEM']
                collections.insert_many(disney.to_dict('Results'))
    except:
        for i in range(1, 149):
            dados = requests.get(f'https://api.disneyapi.dev/characters?page={i}').json()
            for var in range(0, 49):
                nome = dados['data'][var]['name']
                filme = dados['data'][var]['films']
                shows = dados['data'][var]['tvShows']
                allies = dados['data'][var]['allies']
                enemies = dados['data'][var]['enemies']
                imagem = dados['data'][var]['sourceUrl']

                disney = {'Nome': [nome],
                          'Filmes': [filme],
                          'TV Shows(Séries)': [shows],
                          'Aliados': [allies],
                          'Inimigos': [enemies],
                          'Info Original': [imagem]}

                disney = pd.DataFrame(disney)

                db = client['DISNEY']
                collections = db['PERSONAGEM']
                collections.insert_many(disney.to_dict('Results'))
    print('SEUS DADOS FORAM GRAVADOS COM SUCESSO!')


extrac()










