#criando os cavaleiros, qualquer um

import requests
import pandas as pd
import random

#requisição
persona = requests.get('https://saint-seiya-api.herokuapp.com/api/characters').json()

class Cavaleiro():
    def __init__(self, id):
        persona = requests.get('https://saint-seiya-api.herokuapp.com/api/all-classes').json()
        #construção das variaveis
        self.id = id
        self.nome = persona[id]['name']
        self.constelacao = persona[id]['class']['name']
        self.nascimento = persona[id]['affiliation']['actualDate']
        self.ataque = persona[id]['attacks']
        self.ataque = random.choice(self.ataque)
        self.nivel = persona[id]['rank']
        self.texto = \
        f"""
        Dados do Cavaleiro:
        Nome: {self.nome},
        Constelação: {self.constelacao},
        Nível: {self.nivel}"""
        self.textoAtaque = f"""Eu irei te atacar usando o meu {self.ataque}"""




