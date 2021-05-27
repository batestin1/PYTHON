# Essa é uma api de South Park para quem é verdadeiro fã


#chamando a biblioteca

import requests
from typewriter import MaquinadeEscrever


name = 'Say my name, motherfuck!'
MaquinadeEscrever(name).mensagem
nome = input('(Digite o nome do personagem que deseja consultar:) ')
persona = requests.get(f'https://spapi.dev/api/characters?search={nome}').json()
fullname = persona['data'][0]['full_name']
age = persona['data'][0]['age']
sex = persona['data'][0]['sex']
occupation = persona['data'][0]['occupation']
religion = persona['data'][0]['religion']

textao = f"""
Here idiot, what you need to know about this character:
FULL NAME = {fullname},
AGE = {age},
SEX = {sex},
OCCUPATION = {occupation},
RELIGION = {religion}

Now, get the fuck out here, and have fun!

"""
MaquinadeEscrever(textao).mensagem