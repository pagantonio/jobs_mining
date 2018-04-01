# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

from scrapy.conf import settings


class StatePipeline(object):
    def __init__(self):
        self.states = [{'long': 'Acre', 'short': 'AC'}, {'long': 'Alagoas', 'short': 'AL'},
                       {'long': 'Amapá', 'short': 'AP'}, {'long': 'Amazonas', 'short': 'AM'},
                       {'long': 'Bahia', 'short': 'BA'}, {'long': 'Ceará', 'short': 'CE'},
                       {'long': 'Distrito Federal', 'short': 'DF'}, {'long': 'Espírito Santo', 'short': 'ES'},
                       {'long': 'Goiás', 'short': 'GO'}, {'long': 'Maranhão', 'short': 'MA'},
                       {'long': 'Mato Grosso', 'short': 'MT'}, {'long': 'Mato Grosso do Sul', 'short': 'MS'},
                       {'long': 'Minas Gerais', 'short': 'MG'}, {'long': 'Pará', 'short': 'PA'},
                       {'long': 'Paraíba', 'short': 'PB'}, {'long': 'Paraná', 'short': 'PR'},
                       {'long': 'Pernambuco', 'short': 'PE'}, {'long': 'Piauí', 'short': 'PI'},
                       {'long': 'Rio de Janeiro', 'short': 'RJ'}, {'long': 'Rio Grande do Norte', 'short': 'RN'},
                       {'long': 'Rio Grande do Sul', 'short': 'RS'}, {'long': 'Rondônia', 'short': 'RO'},
                       {'long': 'Roraima', 'short': 'RR'}, {'long': 'Santa Catarina', 'short': 'SC'},
                       {'long': 'São Paulo', 'short': 'SP'}, {'long': 'Sergipe', 'short': 'SE'},
                       {'long': 'Tocantins', 'short': 'TO'}]

    def process_item(self, item, spider):
        print('Processing state, item=' + str(item))
        if spider.name not in ['joblinks', 'monster', 'author', 'linkedin', 'quotes']:
            state = next(d for (index, d) in enumerate(self.states) if d['short'] == item['state_short'])
            item['state_long'] = state['long']
        return item


class MongoPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )

        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        print('Saving job to database')
        if spider.name not in ['joblinks', 'monster', 'author', 'linkedin', 'quotes']:
            self.collection.insert(dict(item))
        return item
