# Pypodex

# Este é um projeto de requisição de api e armazenamento de dados em python, consumindo, para isso,
# a API do POKEMON
# link da api = https://pokeapi.co/

# imports

import requests
import pandas as pd
import time
from pymongo import MongoClient
from pokemon import Pokemon
from typewriter import MaquinadeEscrever
import random

#conexao
client = MongoClient('localhost', 27017)

def init():
    global pokebola
    global num
    global guardar
    global pokedex
    num = random.randint(1, 151)
    nome = Pokemon(num).nome
    tipo = Pokemon(num).tipo
    pokedex = Pokemon(num).pokedex
    altura = Pokemon(num).altura
    peso = Pokemon(num).peso
    habilidades = Pokemon(num).habilidades
    ataque = Pokemon(num).ataque
    defesa = Pokemon(num).defesa
    textoPok = f""" Olhe lá... que pokemon será?"""
    print("")
    MaquinadeEscrever(textoPok).mensagem
    textoPok2 = f""" Parece que é um...{nome}..."""
    print('')
    MaquinadeEscrever(textoPok2).mensagem
    textoPok3 = "Deseja Capturar? "
    print('')
    MaquinadeEscrever(textoPok3).mensagem
    print('')
    capturar = input('Escreva SIM ou NÃO:').upper()[0]
    if capturar == 'S':
        textoPegando = f"""
                Você jogou sua pokebola!
                Vamos ver se conseguiu capturar..."""
        MaquinadeEscrever(textoPegando).mensagem
        print('')
        textoDados = f"""
                ...
                    ...
                        ...
                Você capturou!!!
                Este são os dados sobre o pokemon que você capturou!
                Nome: {nome},
                Tipo: {tipo},
                Pokedex: {pokedex},
                Altura: {altura}m
                Peso: {peso}k
                Habilidade: {habilidades}
                Nível de Ataque: {ataque}hp
                Nível de Defesa: {defesa}hp"""
        MaquinadeEscrever(textoDados).mensagem
        print('')
        print('~' * 100)
        textoGuardar = """ Deseja guardar seu pokemon na pokedex? """
        print('')
        MaquinadeEscrever(textoGuardar)
        guardar = input("Escreva SIM ou NÃO: ").upper()[0]
        if guardar == 'S':

            pokedex = {'Treinador': [seunome],
                       'Pokemon': [nome],
                       'Tipo': [tipo],
                       'Pokedex': [pokedex],
                       'Altura': [altura],
                       'Peso': [peso],
                       'Habilidade': [habilidades],
                       'Ataque(hp)': [ataque],
                       'Defesa(hp)': [defesa]}
            pokedex = pd.DataFrame(pokedex)
            db = client['POKEMON']
            collections = db['POKEDEX']
            collections.insert_many(pokedex.to_dict('Results'))
            textoGuardado = f'{seunome} O seu pokemon está salvo na Pokedex MONGO!'
            MaquinadeEscrever(textoGuardado)
            print('')
            print('~'*100)
            repet()

        else:
            textoN = 'Obrigado por jogar!'
            MaquinadeEscrever(textoN).mensagem
    else:
        textoN = 'Obrigado por jogar!'
        MaquinadeEscrever(textoN).mensagem



def intro():
    global seunome
    print('~' * 300)
    time.sleep(1)
    textoIntro = 'Welcome to PokeWord'
    MaquinadeEscrever(textoIntro).mensagem
    print('')
    time.sleep(1)
    print('~' * 300)
    print('')
    textoIntro2 = """
    Este é o mundo dos pokemons!
    Cada pokemon é único e especial.
    Qual é o seu nome? """
    print('')
    MaquinadeEscrever(textoIntro2)
    time.sleep(1)
    print('')
    print('~' * 300)
    print('')
    seunome = input('Entre com seu nome: ').upper()
    print('')
    print('~' * 300)
    time.sleep(1)
    print('')
    textointro3 = f"""
    {seunome}, Você acaba de receber uma pokebola para explorar
    este mundo maravilhoso dos pokemons.
    Esta pronto para capturar pokemons?"""
    MaquinadeEscrever(textointro3)
    print('')
    resposta = input('Escreva SIM ou NÃO: ').upper()[0]
    time.sleep(1)
    print('')
    if resposta == 'S':
        init()
    else:
        textoSaida = "Muito bem! obrigado por participar!"
        MaquinadeEscrever(textoSaida).mensagem

def repet():
    global desejar
    textoDesejar = 'Deseja jogar novamente? '
    MaquinadeEscrever(textoDesejar).mensagem
    print('')
    desejar = input('Escreva SIM ou NÃO: ').upper()[0]
    while desejar == 'S':
        init()

    print('')
    textoN = 'Obrigado por jogar!'
    MaquinadeEscrever(textoN).mensagem

if __name__== '__main__':
    intro()