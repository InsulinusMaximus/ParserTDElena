import logging
import collections
import bs4
import requests
import re
from Parser import config

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Oddis')

# To write the parsed data of one card, the data type is used - a named tuple
product_category_name = 'All_women'
ParseResult = collections.namedtuple(
    product_category_name,
    (
        'url',
        'goods_name',
        'article',
        'price',
        'sizes'
    ),
)


class Parser_Instance:

    def __init__(self):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        # The main return list that contains named tuples with product data
        self.result = []

    # Method that loads a page and returns HTML in a text format
    def load_page(self, url):
        try:
            res = self.session.get(url=url)
            res.raise_for_status()
        except ConnectionError:
            res = 1
            print("Connection refused")
        return res.text

    # Bringing the text of the downloaded page to BeautyfulSoup
    # Splitting the page into blocks (cards of a single product)
    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        all_cards = soup.select_one('ul.cat_ul')
        container = all_cards.select('li')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        product_title = block.select_one('div.catalog-capt')
        try:
            link = product_title.select_one('a').get('href')
        except AttributeError:
            link = '-'
        try:
            name = product_title.select_one('a').get_text().strip()
        except AttributeError:
            name = '-'

        try:
            article = block.select_one('div.catalog-art').get_text().replace('АРТ. ', '')
        except AttributeError:
            article = '-'

        try:
            price = block.select_one('div.catalog-price').get_text().replace('цена в розницу', '')
            price = price.replace('₽', '').split('-')
        except AttributeError:
            price = ['-']

        try:
            sizes = block.select_one('div.catalog-size').get_text().replace('Размер: ', '').split('-')
            size = [i+2 for i in range(int(sizes[0]), int(sizes[1])-1)]
        except AttributeError:
            size = ['-']

        # Passing all variables, data store parsing individual elements, variable result (named tuple)
        self.result.append(ParseResult(
            url=link,
            goods_name=name,
            article=article,
            price=price,
            sizes=size
        ))

    def run(self):
        # for url in config.NatalyFutbolka:
        text = self.load_page(url='https://oddis.ru/produkciya/zhenshchinam')
        self.parse_page(text=text)
        for card_data in self.result:
            logger.info(card_data)
        logger.info(f'Got {len(self.result)} elements')


if __name__ == '__main__':
    parser = Parser_Instance()
    parser.run()
