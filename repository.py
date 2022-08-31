# coding: utf-8
import csv
import logging
import os
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
    'Артикул ТД Валерия',
    'Цена ТД Валерия',
    'Ссылка на артикул ТД Валерия',
    'Артикул Оддис',
    'Цена Оддис',
    'Ссылка на артикул Оддис',
    'Артикул Модно',
    'Цена Модно',
    'Ссылка на артикул Модно',
    'Артикул Инстанс',
    'Цена Инстанс',
    'Ссылка на артикул Инстанс',
)


def directory_creation(category):
    """
    Need to create a directory to write the created CSV file into it and return the path to it,
    if the directory is already created on the device, then just return the path to it
    """
    current_directory = str(os.getcwd())
    if 'Result_in_CSV_format' in current_directory.split('\\'):
        return current_directory.replace('\\',
                                         '/') + f'/{category}_parsing_from_{datetime.now().strftime("%d.%m.%Y-%H.%M")}.csv'

    try:
        os.mkdir('Result_in_CSV_format')
        os.chdir('Result_in_CSV_format')
        return str(os.getcwd()).replace('\\',
                                        '/') + f'/{category}_parsing_from_{datetime.now().strftime("%d.%m.%Y-%H.%M")}.csv'
    except OSError:
        os.chdir('Result_in_CSV_format')
        return str(os.getcwd()).replace('\\',
                                        '/') + f'/{category}_parsing_from_{datetime.now().strftime("%d.%m.%Y-%H.%M")}.csv'


class Repository:

    @staticmethod
    def save_general_data(write_list, category):
        path = directory_creation(category)
        with open(path, 'w', encoding="utf-8", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, delimiter=';', dialect='excel')
            writer.writerow(HEADERS)
            for item in write_list:
                writer.writerow(item)
        print(f'__________{category} category was saved in csv file__________')

    def run(self, final_list, category):
        self.save_general_data(final_list, category)
