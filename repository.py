# coding: utf-8
import csv
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Repository')

HEADERS = (
    'Название',
    'Артикул ТД Елена',
    'Цена ТД Елена',
    'Артикул Натали',
    'Цена Натали',
    'Ссылка на артикул Натали',
    'Артикул Гомани',
    'Цена Гомани',
    'Ссылка на артикул Гомани',
)


class Repository:

    @staticmethod
    def save_general_data(write_list):
        path = f'C:/Users/Pavel/PycharmProjects/TDElenaParser/Parsing_from_{datetime.now().strftime("%Y.%m.%d-%H.%M.%S")}.csv'
        with open(path, 'w', encoding="utf-8", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, delimiter=';')
            writer.writerow(HEADERS)
            for item in write_list:
                writer.writerow(item)

    def run(self, final_list):
        self.save_general_data(final_list)
        logger.info('__________Saved to repository___________')
