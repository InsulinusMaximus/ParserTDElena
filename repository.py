# coding: utf-8
import csv
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Repository')

HEADERS = (
    'company',
    'goods_name',
    'article',
    'price',
    'sizes',
    'url',
)


class Repository:

    def __init__(self, tdelena_result, second_company_result, articles_config: dict):
        self.tdelena_result = tdelena_result
        self.second_company_result = second_company_result
        self.articles_config = articles_config

    def search_articles(self):
        general_data = []
        for td_elena_article, second_company_article in self.articles_config.items():
            for data in self.tdelena_result:
                if data.article == td_elena_article:
                    general_data.append(data)
                    break
            for data in self.second_company_result:
                if data.article == second_company_article:
                    general_data.append(data)
                    break
        return general_data

    @staticmethod
    def save_general_data(general_data):
        path = f'C:/Users/Pavel/PycharmProjects/TDElenaParser/test_save{datetime.now().strftime("%Y%m%d-%H%M%S")}.csv'
        with open(path, 'w', encoding="utf-8", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, delimiter=';')
            writer.writerow(HEADERS)
            for item in general_data:
                writer.writerow(item)

    def run(self):
        general_data = self.search_articles()
        self.save_general_data(general_data=general_data)
        logger.info('\n'.join(map(str, general_data)))
