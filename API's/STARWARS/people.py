# STARPEDIA

# Este é um projeto de requisição de api e armazenamento de dados em python, consumindo, para isso,
# a API do STARWARS
# link da api = https://swapi.dev/


import requests
import pandas as pd
from pymongo import MongoClient

#api
dados = requests.get('https://swapi.dev/api/people/').json()

#working connection
client = MongoClient('localhost', 27017)

tamanho = len(dados['results'])

for i in range(tamanho):

    nome = dados['results'][i]['name']
    anoNascimento = dados['results'][i]['birth_year']
    genero = dados['results'][i]['gender']
    altura = dados['results'][i]['height']
    peso = dados['results'][i]['mass']
    corCabelo = dados['results'][i]['hair_color']
    eye = dados['results'][i]['eye_color']
    persona1 = {'NOME': [nome],
                'DATA DE NASCIMENTO': [anoNascimento],
                'GENERO': [genero],
                'ALTURA': [altura],
                'PESO': [peso],
                'COR DE CABELO': [corCabelo],
                'COR DOS OLHOS': [eye]}
    persona1 = pd.DataFrame(persona1)
    db = client['StarWars']
    collections = db['persona']
    collections.insert_many(persona1.to_dict('Results'))


print("""Your result was also saved in a STARPEDIA, 
    thank you for the preference and may the force be with you.""")