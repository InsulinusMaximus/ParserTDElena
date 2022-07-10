import logging
import collections
import bs4
import requests
import Parser.Config.GomanyConfig as GomanyConfig
'''
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Gomany')

company = 'Gomany'

# To write the parsed data of one card, the data type is used - a named tuple
product_category_name = 'All'
ParseResult = collections.namedtuple(
    product_category_name,
    (
        'company',
        'article',
        'goods_name',
        'price',
        'sizes'
        'url'
    ),
)


class Parser_Gomany:

    def __init__(self, articles_data):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        self.articles_data = articles_data
        # The main return list that contains named tuples with product data
        self.parsing_result = []
        self.result_gomany = []

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
        self.parsing_result.append(ParseResult(
            company=company,
            article=article,
            goods_name=name,
            price=price,
            sizes=sizes,
            url=link
        ))

    def article_filtering(self, parsing_result):
        for card_data in parsing_result:
            if card_data.article in self.articles_data:
                self.result_gomany.append(card_data)

    def run(self):
        # for url in GomanyConfig.:
        text = self.load_page(url=)
        self.parse_page(text=text)
        for card_data in self.parsing_result:
            logger.info(card_data)
        logger.info(f'Got {len(self.parsing_result)} elements')


if __name__ == '__main__':
    parser = Parser_Gomany()
    parser.run()
'''