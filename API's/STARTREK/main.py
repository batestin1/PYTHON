#PROJETO STARTREK
#API DE CONSUMO http://stapi.co/api/v1/rest/character/search/


#CHAMANDO BIBLIOTECA

import requests
import pandas as pd
from pymongo import MongoClient
import pymongo

#working connection
client = MongoClient('localhost', 27017)
#construindo api
dados = requests.get('http://stapi.co/api/v1/rest/character/search/').json()

name = []
genero = []
altura = []
peso = []
sangue = []
lugar = []
real = []
for i in range(24):
    name = dados['characters'][i]['name']
    genero = dados['characters'][i]['gender']
    altura = dados['characters'][i]['height']
    peso = dados['characters'][i]['weight']
    morto = dados['characters'][i]['deceased']
    sangue = dados['characters'][i]['bloodType']
    lugar = dados['characters'][i]['placeOfBirth']
    real = dados['characters'][i]['fictionalCharacter']


    persona = {'Nome do Personagem': [name],
               'Genero': [genero],
               'Altura': [altura],
               'Peso': [peso],
               'Personagem esta morto?': [morto],
               'Tipo de Sangue': [sangue],
               'Lugar de Nascimento': [lugar],
               'Personagem é real': [real]}
    persona = pd.DataFrame(persona)
    db = client['STARTREK']
    collections = db['PERSONAGEM']
    collections.insert_many(persona.to_dict('Results'))

print('Sucesso!')
