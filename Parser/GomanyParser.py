import logging
import collections
import bs4
import requests

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Gomany')

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
        container = soup.select('li.product.type-product')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        title = block.select_one('div.title-h2')
        try:
            link = title.select_one('a').get('href')
        except AttributeError:
            link = '-'
        try:
            name = title.select_one('a').get_text().strip()
        except AttributeError:
            name = '-'

        try:
            article = block.select_one('span', class_='sku').get_text().strip().replace('Артикул: ', '')
        except AttributeError:
            article = '-'

        try:
            price = block.select_one('span.price').get_text().strip().replace('₽', '').replace(',', '').split(' – ')
        except AttributeError:
            price = ['-']

        try:
            sizes = block.select_one('div.sku').get_text().replace('Размеры: ', '').split(', ')
        except AttributeError:
            sizes = ['-']

        # Passing all variables, data store parsing individual elements, variable result (named tuple)
        self.result.append(ParseResult(
            url=link,
            goods_name=name,
            article=article,
            price=price,
            sizes=sizes
        ))

    def run(self):
        # for url in config.NatalyFutbolka:
        text = self.load_page(url='https://gomani.ru/product-category/womens/')
        self.parse_page(text=text)
        for card_data in self.result:
            logger.info(card_data)
        logger.info(f'Got {len(self.result)} elements')


if __name__ == '__main__':
    parser = Parser_Instance()
    parser.run()
