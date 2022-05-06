import logging
import collections
import bs4
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Natali')

ParseResult = collections.namedtuple(
    'ParseResult',
    (
        'url',
        'goods_name',
        'price',
        'size'
    ),
)


class Parser_Nataly_Futbolki:

    def __init__(self):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        self.result = []

    # Method that loads a page and returns HTML in a text format
    def load_page(self, page: int = None):
        url = 'https://natali37.ru/catalog/category/174'
        try:
            res = self.session.get(url=url)
            res.raise_for_status()
        except:
            print('Error')
        return res.text

    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('li.product-card.product-card--with-overlay')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        parse_link_goods_name_pricetable_sizes = block.select_one('div.product-card__wrapper')
        if not parse_link_goods_name_pricetable_sizes:
            logger.error('No product card wrapper')
            return

        parse_link_name = parse_link_goods_name_pricetable_sizes.select_one('a.product-card__name.link')
        if not parse_link_name:
            logger.error('No product card name and link')
            return

        link = parse_link_name.get('href')
        if not link:
            logger.error('No link')
            return
        link = 'https://natali37.ru/' + link

        name = parse_link_name.get_text()
        if not name:
            logger.error('No name')
            return
        name = name.split()

        price_table = parse_link_goods_name_pricetable_sizes.select('div.price-table__column')
        if not price_table:
            logger.error('No price table')
            return
        prices = {}
        for price_and_name in price_table:
            price_name = price_and_name.select_one('div.price-table__name').get_text()
            if not price_name:
                logger.error('No price name')
                return
            price_name = price_name.strip()

            price = price_and_name.select_one('div.price-table__value').get_text()
            if not price:
                logger.error('No price')
                return
            price = price.strip()

            prices.update({price_name: price})

        sizes = parse_link_goods_name_pricetable_sizes.select_one('ul.sizes__list.list').get_text()
        if not sizes:
            logger.error('No sizes')
            return
        sizes = " ".join(sizes.split()).split()

        self.result.append(ParseResult(
            url=link,
            goods_name=name,
            price=prices,
            size=sizes
        ))

        # logger.debug('%s, %s, %s, %s', link, name, prices, sizes)
        # logger.debug('-' * 100)

        # logger.info(self.result)

    def run(self):
        text = self.load_page()
        self.parse_page(text=text)
        logger.info(f'Got {len(self.result)} elements')

        # self.save_result()
