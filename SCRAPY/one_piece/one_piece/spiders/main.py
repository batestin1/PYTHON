import scrapy

import pandas as pd
from pymongo import MongoClient
#conexao
client = MongoClient('localhost', 27017)

class MainSpider(scrapy.Spider):
    name = 'main'
    nome = input('Digite o nome do personagem que você deseja consultar: ')
    start_urls = [f'https://onepiece.fandom.com/pt/wiki/{nome}']



    def parse(self, response, **kwargs):
        global dados
        global nomeJapones
        global nomePortugues
        global apelido
        global situacao
        global aniversario
        global altura
        global akuma
        global onepiece

        try:
            dados = response.xpath('//div[@class="pi-data-value pi-font"]/text()').getall()
            nomeJapones = dados[0]
            nomePortugues = dados[2]
            apelido = dados[22]
            situacao = dados[26]
            aniversario = dados[32]
            altura = dados[33]
            akuma = dados[45]

            onepiece = {
                'Nome Original': nomeJapones,
                'Nome em Português': nomePortugues,
                'Apelido': apelido,
                'Status': situacao,
                'Aniversário': [aniversario],
                'Altura': [altura],
                'Akuma no mi': akuma}

            onepiece = pd.DataFrame(onepiece)
            db = client['ONEPIECE']
            collections = db['personagem']
            collections.insert_many(onepiece.to_dict('Results'))
        except:
            dados = response.xpath('//div[@class="pi-data-value pi-font"]/text()').getall()
            nomeJapones = dados[0]
            nomePortugues = dados[2]
            apelido = dados[22]
            situacao = dados[26]
            aniversario = dados[32]

            onepiece = {
                'Nome Original': nomeJapones,
                'Nome em Português': nomePortugues,
                'Apelido': apelido,
                'Status': situacao,
                'Aniversário': [aniversario]
            }

            onepiece = pd.DataFrame(onepiece)
            db = client['ONEPIECE']
            collections = db['personagem']
            collections.insert_many(onepiece.to_dict('Results'))












