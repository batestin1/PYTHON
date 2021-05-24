
# CHRONICS OF API

# Este é um projeto de requisição de api e armazenamento de dados em python, consumindo, para isso,
# a API do GAME OF THORNES
# link da api = https://anapioficeandfire.com/

#chamando bilioteca
import requests
import json
import time
import pandas as pd
from pymongo import MongoClient
import pymongo
from os import listdir
from os.path import isfile, join
from os import walk


#working connection
client = MongoClient('localhost', 27017)

#criando funções
def open():
    time.sleep(1)
    print('~' * 35)
    time.sleep(1)
    print('~' * 12 + 'GAME OF THRONES - BANCO DE DADOS' + '~' * 16)
    time.sleep(1)
    print('~' * 35)
    time.sleep(1)
    print('~' + 'Developed by Maycon Cypriano' + '~~')
    print('~' * 35)
    print('')
    time.sleep(1)
    print('O INVERNO ESTÁ CHEGANDO!')
    time.sleep(1)
    print("""AQUI ESTÁ O CANAL POR ONDE VOCÊ VAI ARMAZENAR TODOS OS DADOS
    DOS PERSONAGENS E CASAS DE GAME OF THRONES""")
    processar()

def processar():
    time.sleep(1)
    print('~' * 35)
    resposta = input('Deseja continuar?(s/n)' ).upper()[0]
    if resposta == 'S':
        print("Estamos processando a operacao!")
        time.sleep(1)
        print('~' * 35)
        print('...')
        time.sleep(1)
        print('~' * 35)
        personagem()
        personagem2()
        personagem3()
        casas()
        print('Dados processados com sucesso!')
        time.sleep(1)
        print('Você pode conferir tudo no banco de dados MONGO!')
        time.sleep(1)
        print('Obrigado!')

    else:
        print("Obrigado!")

def personagem2():
    num = 1511


    for i in range(1511, 1994):
        num = num + 1
        people = requests.get(f'https://anapioficeandfire.com/api/characters/{num}').json()
        # variaveis dos personagens
        name = people['name']
        apelido = people['aliases']
        titulo = people['titles']
        genero = people['gender']
        culture = people['culture']
        born = people['born']
        url = people['url']

        # construindo os personagens

        persona = {'Nome Completo': [name],
                   'Cultura': [culture],
                   'Titulo Oficial': [titulo],
                   'Apelidos': [apelido],
                   'Genero': [genero],
                   'Ano de Nascimento': [born],
                   'Identificador': [url]}

        persona = pd.DataFrame(persona)
        db = client['GAMEOFTHRONES']
        collections = db['PERSONAGENS']
        collections.insert_many(persona.to_dict('Results'))

def personagem3():
    num = 1995


    for i in range(1995, 2137):
        num = num + 1
        people = requests.get(f'https://anapioficeandfire.com/api/characters/{num}').json()
        # variaveis dos personagens
        name = people['name']
        apelido = people['aliases']
        titulo = people['titles']
        genero = people['gender']
        culture = people['culture']
        born = people['born']
        url = people['url']

        # construindo os personagens

        persona = {'Nome Completo': [name],
                   'Cultura': [culture],
                   'Titulo Oficial': [titulo],
                   'Apelidos': [apelido],
                   'Genero': [genero],
                   'Ano de Nascimento': [born],
                   'Identificador': [url]}

        persona = pd.DataFrame(persona)
        db = client['GAMEOFTHRONES']
        collections = db['PERSONAGENS']
        collections.insert_many(persona.to_dict('Results'))


def personagem():
    num = 1


    for i in range(1507):
        num = num + 1
        people = requests.get(f'https://anapioficeandfire.com/api/characters/{num}').json()
        # variaveis dos personagens
        name = people['name']
        apelido = people['aliases']
        titulo = people['titles']
        genero = people['gender']
        culture = people['culture']
        born = people['born']
        url = people['url']

        # construindo os personagens

        persona = {'Nome Completo': [name],
                   'Cultura': [culture],
                   'Titulo Oficial': [titulo],
                   'Apelidos': [apelido],
                   'Genero': [genero],
                   'Ano de Nascimento': [born],
                   'Identificador': [url]}

        persona = pd.DataFrame(persona)
        db = client['GAMEOFTHRONES']
        collections = db['PERSONAGENS']
        collections.insert_many(persona.to_dict('Results'))

def casas():

    num1 = 1
    for i in range(443):

        num1 = num1+1

        casa = requests.get(f'https://www.anapioficeandfire.com/api/houses/{num1}').json()



        #variaveis das casas
        house = casa['name']
        regiao = casa['region']
        armas = casa['ancestralWeapons'][0]
        brasao = casa['coatOfArms']
        words = casa['words']
        senhor = casa['currentLord']
        fundado = casa['founded']
        membros = casa['swornMembers']



        # construindo as casas
        familia = { 'CASA': [house],
                   'REGIÃO':[regiao],
                    'ARMAS ANCENTRAIS': [armas],
                   'BRASÃO':[brasao],
                   'LEMA':[words],
                    'SENHOR(a)': [senhor],
                   'FUNDADO POR':[fundado],
                    'MEMBROS': [membros]}

        familia = pd.DataFrame(familia)
        db = client['GAMEOFTHRONES']
        collections = db['CASAS']
        collections.insert_many(familia.to_dict('Results'))



open()
