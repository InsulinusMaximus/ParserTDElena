import logging
import collections
import bs4
import requests


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Modno')

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


class Parser_Modno:

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
        all_cards = soup.select_one('ul.list_tiles')
        container = all_cards.select('li.position_item')
        for block in container:
            self.parse_block(block=block)

    # Parsing of each block (cards of a single product)
    def parse_block(self, block):

        product_title = block.select_one('div.position_item_photo')
        title = product_title.select_one('a')
        try:
            link = 'https://modno-trikotazh.ru' + title.get('href')
        except AttributeError:
            link = '-'
        try:
            name = title.select_one('span.title').get_text().strip()
        except AttributeError:
            name = '-'

        article = name

        content = block.select_one('div.item_content')
        try:
            price = content.select_one('span.cennik').get_text().strip().replace('от ', '').replace(' ₽', '')
            price = price.replace(' ', '')
        except AttributeError:
            price = '-'

        chars = content.select_one('div.chars')
        sizes_container = chars.select_one('span.chars___filter_size_test')
        try:
            sizes = sizes_container.select_one('span.chars_char_data').get_text().strip().split(', ')
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
        text = self.load_page('https://modno-trikotazh.ru/platja')
        self.parse_page(text=text)
        for card_data in self.result:
            logger.info(card_data)
        logger.info(f'Got {len(self.result)} elements')


if __name__ == '__main__':
    parser = Parser_Modno()
    parser.run()
