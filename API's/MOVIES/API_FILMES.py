# Movie

# Este é um projeto de requisição de api e armazenamento de dados em python, consumindo, para isso,
# a API do filmes
# link da api = http://www.omdbapi.com/

#chamando biblioteca
import requests
import json
import time
from pymongo import MongoClient
import pymongo
import pandas as pd

#conexao
client = MongoClient('localhost', 27017)
time.sleep(1)
print('~' * 35)
time.sleep(1)
print('~' * 12 + 'CINEMA' + '~' * 16)
time.sleep(1)
print('~' * 35)
time.sleep(1)
print('~' + 'Desenvolvido por Maycon Cypriano' + '~~')
print('~' * 35)
time.sleep(1)
print('')
time.sleep(1)
print('Quer saber tudo sobre seu filme favorito?')
time.sleep(1)
print('~' * 35)
time.sleep(1)
print('~' * 35)
fi = input("ENTÃO, DIGA PARA MIM O NOME DO SEU FILME (EM INGLÊS, POR FAVOR): ").lower()
filme = f'http://www.omdbapi.com/?t={fi}&apikey=481754c7'
res = requests.get(filme)
movie = json.loads(res.text)
titulo = movie['Title']
ano = movie['Year']
clas = movie['Rated']
genero = movie['Genre']
roteiro = movie['Writer']
diretor = movie['Director']
elenco = movie['Actors']
tabela = {'Titulo': [titulo],
          'Ano': [ano],
          'Classificação': [clas],
          'Genero': [genero],
          'Diretor': [diretor],
          'Roteiro':[roteiro],
          'Elenco': [elenco]}
tabela= pd.DataFrame(tabela)
db = client['BancodeFilmes']
collections = db['Filmes']
collections.insert_many(tabela.to_dict('Results'))
tabela.to_excel('Movies.xlsx', index=False)

print('~' * 35)
time.sleep(1)
print('Aqui estão suas informações')
time.sleep(1)
print('Titulo:', movie['Title'])
print('~' * 35)
time.sleep(1)
print('Ano: ', movie['Year'])
print('~' * 35)
time.sleep(1)
print('Classificação:', movie['Rated'])
print('~' * 35)
time.sleep(1)
print('Genero:', movie['Genre'])
print('~' * 35)
time.sleep(1)
print('Diretor: ', movie['Director'])
print('~' * 35)
time.sleep(1)
print('Roteiro: ', movie['Writer'])
print('~' * 35)
time.sleep(1)
print('Elenco: ', movie['Actors'])
print('~' * 35)
time.sleep(1)
print('')


