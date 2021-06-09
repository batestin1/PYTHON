import scrapy
import pandas as pd
from pymongo import MongoClient
#conexao
client = MongoClient('localhost', 27017)


class MlSpider(scrapy.Spider):
    name = 'ml'

    start_urls = [f'https://www.mercadolivre.com.br/ofertas?page={i}' for i in range(1,210)]

    def parse(self, response, **kwargs):
        global preco
        global titulo
        global linka
        global tabela
        link = '//li[@class="promotion-item"]'
        for i in response.xpath(link):
            preco = i.xpath('.//span[@class="promotion-item__price"]//text()').getall()
            titulo = i.xpath('.//p[@class="promotion-item__title"]/text()').get()
            linka = i.xpath('./a/@href').get()


            tabela={
                'preço': preco,
                'produto': titulo,
                'link': linka
            }
            tabela = pd.DataFrame(tabela)
            db = client['MERCADOLIVRE']
            collections = db['produto']
            collections.insert_many(tabela.to_dict('Results'))
