# Pypodex

# Este é um projeto de requisição de api e armazenamento de dados em python, consumindo, para isso,
# a API do POKEMON
# link da api = https://pokeapi.co/

# imports

import requests
import pandas as pd
import time
from pymongo import MongoClient
import pymongo


#conexao
client = MongoClient('localhost', 27017)


# variables
habilidades = ''
poke = ''
numero = ''
tipo = ''



# functions
def intro():
    time.sleep(1)
    print('~' * 35)
    time.sleep(1)
    print('~' * 12 + 'PyPODEX' + '~' * 16)
    time.sleep(1)
    print('~' * 35)
    time.sleep(1)
    print('~' + 'Desenvolvido por Maycon Cypriano' + '~~')
    print('~' * 35)
    time.sleep(1)
    print('')
    print('')
    time.sleep(1)
    print('VOCÊ ENCONTROU UM POKÉMON?')
    time.sleep(1)
    print('~' * 35)
    main()
    print('~' * 35)
    time.sleep(1)
    print('ESTAMOS PROCESSANDO SEU POKEMON')
    print('~' * 35)
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('~' * 35)
    time.sleep(1)
    print('POKEMON PROCESSADO COM SUCESSO!')
    time.sleep(1)
    tab()
    print('SEU POKEMON ESTA A SALVO EM NOSSA PYPODEX!')
    time.sleep(1)
    print('~' * 35)
    time.sleep(1)
    print("OBRIGADO!")



def poder(po):  # função que capta a habilidade do pokemon e o nome de seu poder
    global habilidades
    for i in po['abilities']:
        habilidades = (i['ability']['name'])


def tipo(ti):  # função que me retorna o tipo de pokemon
    global tipo
    for i in ti['types']:
        tipo = (i['type']['name'])


def numero(num):  # função que me retorna o tipo de pokemon
    global numero
    for i in num['game_indices']:
        numero = (i['game_index'])


def main():
    global tipo
    global habilidades
    global poke
    global numero
    global pokedex
    global quant

    poke = input("REGISTRE O SEU POKEMON AGORA: ").lower()
    api = f'https://pokeapi.co/api/v2/pokemon/{poke}'
    res = requests.get(api)
    po = res.json()
    ti = res.json()
    num = res.json()
    poder(po)
    numero(num)
    tipo(ti)


def tab():
    global tipo
    global habilidades
    global poke
    global numero
    global pokedex
    global quant
    pokedex1 = {'POKÉMON': [poke],
                   'NÚMERO': [numero],
                   'TIPO': [tipo],
                   'HABILIDADES': [habilidades]}
    pokedex1 = pd.DataFrame(pokedex1)
    db = client['Pokemon']
    collections = db['Pokedex']
    collections.insert_many(pokedex1.to_dict('Results'))

    pokedex1.to_excel('C:\Users\Bates\Documents\Repositorios\PYTHON\API's\POKEMON\PyPodex/PyPodex.xlsx', index=False)




if __name__== '__main__':
    intro()