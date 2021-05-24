# MUSIC

# Este é um projeto de requisição de api e armazenamento de dados em python, consumindo, para isso,
# a API do AUDIO DB
# link da api = https://www.theaudiodb.com/

#chamando bilioteca
import requests
import pandas as pd
from pymongo import MongoClient
import pymongo

#working connection
client = MongoClient('localhost', 27017)


#criando funções



def artista():
    global nome
    global banda
    global anoFormacao
    global anoMorte
    global estilo
    global site
    global biografia
    global bandaArtista
    nome = input('Qual o nome da banda, ou artista que deseja consultar? ')
    artista = requests.get(f'https://www.theaudiodb.com/api/v1/json/1/search.php?s={nome}').json()

    banda = artista['artists'][0]['strArtist']
    anoFormacao = artista['artists'][0]['intFormedYear']
    anoMorte = artista['artists'][0]["intDiedYear"]
    estilo = artista['artists'][0]["strStyle"]
    site = artista['artists'][0]["strWebsite"]
    biografia = artista['artists'][0]["strBiographyEN"]

    bandaArtista = {'Artista/Banda': [banda],
                'Ano de Formação': [anoFormacao],
                'Ano do Termino': [anoMorte],
                'Estilo Musical': [estilo],
                'Site OficiaL': [site],
                'Biografia Oficial': [biografia]}

    bandaArtista  = pd.DataFrame(bandaArtista)
    db = client['MÚSICA']
    collections = db['BANDA']
    collections.insert_many(bandaArtista.to_dict('Results'))

    return print(f""" Aqui estão as informações sobre sua busca:
                Artista/Banda: {banda},
                Ano de Formação: {anoFormacao},
                Ano do Termino: {anoMorte},
                Estilo Musical: {estilo},
                Site Oficial: {site},
                Biografia Oficial: {biografia}""")
def discografia():
    global banda
    global total
    global disco
    global nomeAlbum
    global anoLancamento
    global name
    global ano
    global discografia
    banda = input('Qual nome da banda deseja conhecer os discos?' )
    total = int(input('Quantos discos deseja ver? '))
    name = []
    ano = []
    for i in range(total):
        disco = requests.get(f'https://theaudiodb.com/api/v1/json/1/discography.php?s={banda}').json()
        nomeAlbum = disco['album'][i]['strAlbum']
        anoLancamento = disco['album'][i]['intYearReleased']
        name.append(nomeAlbum)
        ano.append(anoLancamento)

        discografia = {'Nome do álbum': [name],
                        'Ano de Lançamento': [ano]}

        discografia = pd.DataFrame(discografia)
        db = client['MÚSICA']
        collections = db['DISCOGRAFIA']
        collections.insert_many(discografia.to_dict('Results'))

    return print(f""" Aqui estão as informações sobre sua busca:
                        Nome do Álbum: {name},
                        Ano de Lançamento: {ano}""")



print('Welcome to the Music')
print('Este é um projeto de consulta de Api de Música')
print('Temos duas opções para você consultar')
opcao = int(input("""
[1] - Bandas/Artista 
[2] - Discografia
R: """))
if opcao == 1:
    artista()
elif opcao == 2:
    discografia()
else:
    print("Tente uma opção válida!")


