import logging
import collections
import bs4
import time
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from Parser import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Beloshveika')

# To write the parsed data of one card, the data type is used - a named tuple
product_category_name = 'Woman'
ParseResult = collections.namedtuple(
    product_category_name,
    (
        'url',
        'goods_name',
        'price',
        'size'
    ),
)


class Parser_Beloshveika:

    def __init__(self):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            'Referer': 'https://beloshweyka.ru/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/101.0.4951.67 Safari/537.36'
        }
        self.retry = Retry(connect=3, backoff_factor=0.5)
        self.adapter = HTTPAdapter(max_retries=self.retry)
        self.session.mount('http://', self.adapter)
        self.session.mount('https://', self.adapter)
        # The main return list that contains named tuples with product data
        self.result = []

    # Method that loads a page and returns HTML in a text format
    def load_page(self):
        try:
            res = self.session.get(url='http://beloshweyka.ru/3-zhenskij-trikotazh', verify=False)
            logger.info(res)
            res.raise_for_status()

        except ConnectionError:
            print("Connection refused")
        return res.text

    # Bringing the text of the downloaded page to BeautyfulSoup
    # Splitting the page into blocks (cards of a single product)
    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('li.ajax_block_product.item-inner.col-xs-6')
        logger.info(type(container))
        # for block in container:
        # self.parse_block(block=block)

    def run(self):
        # for url in config.NatalyFutbolka:
        text = self.load_page()
        self.parse_page(text=text)
        logger.info(f'Got {len(self.result)} elements')


if __name__ == '__main__':
    parser = Parser_Beloshveika()
    parser.run()
