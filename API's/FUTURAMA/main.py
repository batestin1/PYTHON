# essa é uma api simples para armazenamento de dados em Mongo dos personagens da serie animada
#futurama.
#este é o endereço da api = http://futuramaapi.herokuapp.com/api/v2/characters


#chama biblioteca

import requests
from pymongo import MongoClient
import pandas as pd

#requisição
dados = requests.get('http://futuramaapi.herokuapp.com/api/v2/characters').json()

#conexao
client = MongoClient('localhost', 27017)

for i in range(20):
    nome = dados[i]["Name"]
    especie = dados[i]["Species"]
    idade = dados[i]["Age"]
    planeta = dados[i]["Planet"]
    profissao = dados[i]['Profession']
    status = dados[i]["Status"]
    futurama = {'Personagem': [nome],
                'Idade': [idade],
                'Raça': [especie],
                'Planeta de Origem':[planeta],
                'Profissão': [profissao],
                'Situação Atual': [status]}
    db = client['FUTURAMA']
    collections = db['PERSONAGENS']
    futurama = pd.DataFrame(futurama)
    collections.insert_many(futurama.to_dict('Results'))


print('GRAVAÇÃO CONCLUIDA COM SUCESSO!')