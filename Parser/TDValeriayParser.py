import logging
import collections
import bs4
import requests
from Parser import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('TDValeriya')

# To write the parsed data of one card, the data type is used - a named tuple
product_category_name = 'All women'
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
        shope = soup.select_one('section.c-shope')
        catalog = shope.select_one('div.c-catalog')
        container = catalog.select('a')
        for block in container:
            self.parse_block(block=block)

    # Parsing of each block (cards of a single product)
    def parse_block(self, block):
        # Get link from attribute href
        link = 'https://xn--80adfgpq0bk8j.xn--p1ai/'+block.get('href')

        # Getting data from the card page
        res_card_inside = self.load_page(link)
        soup_card_inside = bs4.BeautifulSoup(res_card_inside, 'lxml')

        # Parsing the name from the inner page of the card
        name = soup_card_inside.select_one('h2.c-offer_title').get_text().strip()

        # Parsing the article from the inner page of the card
        article = soup_card_inside.select_one('div.c-offer_article').get_text().strip().replace('Артикул: ', '')

        # Parsing prices from the inner page of the card
        price_mod = soup_card_inside.select_one('div.c-opt.price_mod')
        price = price_mod.find('span', itemprop='price').get_text().replace(" ", "").strip()

        # Parsing the size range from the inner page of the card
        size_mod = soup_card_inside.find('div', id='hide_size_mod')
        size_checkbox = size_mod.select_one('ul.c-styles.checkbox_mod')
        sizes_container = size_checkbox.select('label', class_='size_count')
        sizes = []
        for size in sizes_container:
            size = size.find(value='').get_text().strip()
            sizes.append(size)

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
        text = self.load_page("https://xn--80adfgpq0bk8j.xn--p1ai/products/zhenskij-trikotazh/")
        self.parse_page(text=text)
        for card_data in self.result:
            logger.info(card_data)
        logger.info(f'Got {len(self.result)} elements')


if __name__ == '__main__':
    parser = Parser_TDValeriya()
    parser.run()
