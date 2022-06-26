# coding: utf-8
import csv

HEADERS = (
    'url',
    'goods_name',
    'article',
    'price',
    'size'
)


class Save_Results:

    def __init__(self, result):
        self.result = result

    def save_result(self):
        path = 'C:/Users/Pavel/PycharmProjects/TDElenaParser/test_save_TDElena.csv'
        with open(path, 'w', encoding="utf-8", newline="") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL, delimiter=';')
            writer.writerow(HEADERS)
            for item in self.result:
                writer.writerow(item)

    def run(self):
        self.save_result()
