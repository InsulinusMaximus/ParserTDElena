import logging
import collections
import bs4
import requests
from Parser import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('TDValeriya')

# To write the parsed data of one card, the data type is used - a named tuple
product_category_name = 'AllWoman'
ParseResult = collections.namedtuple(
    product_category_name,
    (
        'url',
        'goods_name',
        'price',
        'size'
    ),
)


class Parser_TDValeriya:

    def __init__(self):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/101.0.4951.67 Safari/537.36'
        }
        # The main return list that contains named tuples with product data
        self.result = []

    # Method that loads a page and returns HTML in a text format
    def load_page(self):
        try:
            res = self.session.get(url='https://xn--80adfgpq0bk8j.xn--p1ai/products/zhenskij-trikotazh/')
            #logger.info(res)
            res.raise_for_status()
        except ConnectionError:
            print("Connection refused")
        return res.text

    # Bringing the text of the downloaded page to BeautyfulSoup
    # Splitting the page into blocks (cards of a single product)
    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        shope = soup.select_one('section.c-shope')
        catalog = shope.select_one('div.c-catalog')
        container = catalog.select('a')
        for block in container:
            self.parse_block(block=block)

    # Parsing of each block (cards of a single product)
    def parse_block(self, block):
        # Get link from attribute href
        link = 'https://xn--80adfgpq0bk8j.xn--p1ai/'+block.get('href')



        logger.info(link)

    def run(self):
        # for url in config.NatalyFutbolka:
        text = self.load_page()
        self.parse_page(text=text)
        #logger.info(f'Got {len(self.result)} elements')


if __name__ == '__main__':
    parser = Parser_TDValeriya()
    parser.run()
