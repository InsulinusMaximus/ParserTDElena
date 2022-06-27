# coding: utf-8
import csv
import logging
from datetime import datetime
import Parser.Config.NatalyConfig as ConfigNataly

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Repository')

HEADERS = (
    'company',
    'url',
    'goods_name',
    'article',
    'price',
    'size'
)


class Repository:

    def __init__(self, tdelena_result, second_company_result, tdelena_config, second_company_config):
        self.tdelena_result = tdelena_result
        self.second_company_result = second_company_result
        self.tdelena_config = tdelena_config
        self.second_company_config = second_company_config
        self.article_list = []
        self.general_data = []

    def overall_article_list(self, tdelena_config, second_company_config):
        length_td_elena_config = len(tdelena_config)
        length_second_company_config = len(second_company_config)

        for article_index in range(length_td_elena_config):
            logger.info(article_index)
            self.article_list.append(tdelena_config[article_index])
            self.article_list.append(second_company_config[article_index])

    def search_articles(self, article_list, tdelena_result, second_company_result):
        for article in article_list:
            if article_list.index(article) % 2 == 0:
                for data in tdelena_result:
                    if data.article == article:
                        self.general_data.append(data)
            else:
                for data in second_company_result:
                    if data.article == article:
                        self.general_data.append(data)

    def save_genera_data(self):
        path = f'C:/Users/Pavel/PycharmProjects/TDElenaParser/test_save{datetime.now().strftime("%Y%m%d-%H%M%S")}.csv'
        with open(path, 'w', encoding="utf-8", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, delimiter=';')
            writer.writerow(HEADERS)
            for item in self.general_data:
                writer.writerow(item)

    def run(self):
        self.overall_article_list(tdelena_config=self.tdelena_config, second_company_config=self.second_company_config)
        self.search_articles(article_list=self.article_list, tdelena_result=self.tdelena_result,
                             second_company_result=self.second_company_result)
        self.save_genera_data()
        logger.info('\n'.join(map(str, self.general_data)))
