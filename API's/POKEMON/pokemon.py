#criando os pokemons

import requests
import random

class Pokemon():
    def __init__(self, num):

        self.num = num
        self.api = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.num}').json()
        self.nome = self.api['forms'][0]['name']
        self.peso = self.api['weight']
        self.altura = self.api['height']
        self.pokedex = self.api['game_indices'][3]['game_index']
        self.tipo = self.api['types'][0]['type']['name']
        self.habilidades = self.api['abilities'][0]['ability']['name']
        self.ataque = self.api['stats'][1]['base_stat']
        self.defesa = self.api['stats'][2]['base_stat']









