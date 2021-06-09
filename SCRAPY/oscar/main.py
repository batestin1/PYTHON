import requests as re
from bs4 import BeautifulSoup as sp
import pandas as pd
from pymongo import MongoClient

#conexao
client = MongoClient('localhost', 27017)

def oscar():
    try:
        for i in range(1, 91):
            link = f'https://www.cineplayers.com/premiacoes/oscar/{i}'
            r = re.get(link)

        sopa = sp(r.content, 'html.parser')

        elementos = sopa.find_all('h3', class_='title h4')
        textao = sopa.find_all('a', class_="h5 d-block mb-0")

        listaA = []
        listaB = []

        for elemento in elementos:
            listE = elemento.text
            listaA.append(listE)

        for h in textao:
            listH = h.text
            listaB.append(listH)

        tab = {
            listaA[0]: listaB[0],
            listaA[1]: listaB[1],
            listaA[2]: listaB[2],
            listaA[3]: listaB[3],
            listaA[4]: listaB[4],
            listaA[5]: listaB[5],
            listaA[6]: listaB[6],
            listaA[7]: listaB[7],
            listaA[8]: listaB[8],
            listaA[9]: listaB[9],
            listaA[10]: listaB[10],
            listaA[11]: listaB[11],
            listaA[12]: listaB[12],
            listaA[13]: listaB[13],
            listaA[14]: listaB[14],
            listaA[15]: listaB[15],
            listaA[16]: listaB[16],
            listaA[17]: listaB[17],
            listaA[18]: listaB[18],
            listaA[19]: listaB[19],
            listaA[20]: listaB[20],
            listaA[21]: listaB[21],
            listaA[22]: listaB[22],
            listaA[23]: listaB[23]}

        tab = pd.DataFrame(tab)
        db = client['OSCAR']
        collections = db['PREMIACAO']
        collections.insert_many(tab.to_dict('Results'))

    except: ValueError



oscar()




