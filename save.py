# coding: utf-8
import csv
from datetime import datetime

HEADERS = (
    'company',
    'url',
    'goods_name',
    'article',
    'price',
    'size'
)


class Save_Results:

    def __init__(self, result, nataly_result):
        self.result = result
        self.nataly_result = nataly_result

    def save_result(self):
        path = f'C:/Users/Pavel/PycharmProjects/TDElenaParser/test_save{datetime.now().strftime("%Y%m%d-%H%M%S")}.csv'
        with open(path, 'w', encoding="utf-8", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, delimiter=';')
            writer.writerow(HEADERS)
            for item in self.result:
                writer.writerow(item)

    def run(self):
        self.save_result()
