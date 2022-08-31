import logging
import collections
import bs4
import requests
import Parser.Config.TDValeriayConfig as ConfigTDValeriay
from Parser.ArticlesFilter import article_filtering

company = 'TDVALERIAY'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(company)


# To write the parsed data of one card, the data type is used - a named tuple
company_name = company
ParseResult = collections.namedtuple(
    company_name,
    (
        'goods_name',
        'article',
        'price',
        'sizes',
        'url',
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
        # The main return write_list that contains named tuples with product data
        self.parsing_result = []
        self.result_tdvaleriay_women = []
        self.result_tdvaleriay_men = []
        self.result_tdvaleriay_children = []

    # Method that loads a page and returns HTML in a text format
    def load_page(self, url):
        logger.info(f'Connection attempt:{url}')
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
        try:
            catalog = soup.select_one('div.catalog_block')
            container = catalog.select('div.col-lg-3')
        except AttributeError:
            logger.info('There are no required attributes on the page')
            return None

        for block in container:
            self.parse_block(block=block)

    # Parsing of each block (cards of a single product)
    def parse_block(self, block):
        item_info = block.select_one('div.item_info')

        item_title = item_info.select_one('div.item-title')

        link_storage = item_title.select_one('a')

        try:
            link = 'https://tdvaleria.ru'+link_storage.get('href')
        except AttributeError:
            link = '-'

        try:
            name = link_storage.select_one('span').get_text().strip()
        except AttributeError:
            name = '-'

        try:
            article_block = item_info.select_one('div.article_block')
            article = article_block.select_one('div.muted').get_text().strip().replace('Арт.: ', '').strip()
        except AttributeError:
            article = '-'

        try:
            info_bottom_block = item_info.select_one('div.item_info--bottom_block')
            price_wrapper = info_bottom_block.select_one('div.js_price_wrapper')
            prices = price_wrapper.select_one('div.price').get('data-value').strip()
        except AttributeError:
            prices = ['-']

        try:
            footer_button = block.select_one('div.footer_button')
            size_checkbox = footer_button.select_one('div.bx_size_scroller_container')
            sizes_container = size_checkbox.select('li')
            sizes = []
            for size in sizes_container:
                size = size.get('title').strip().replace('Размер: ', '')
                sizes.append(size)
        except AttributeError:
            sizes = ['-']

        # Passing all variables, data store parsing individual elements, variable result (named tuple)
        self.parsing_result.append(ParseResult(
            goods_name=name,
            article=article,
            price=prices,
            sizes=sizes,
            url=link,
        ))

    def run_women_parsing(self):
        for women_url in ConfigTDValeriay.women_urls:
            for url in women_url:
                text = self.load_page(url=url)
                self.parse_page(text=text)

        logger.info(f'Got {len(self.parsing_result)} elements WOMEN category')

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_tdvaleriay_women,
                          article_data=ConfigTDValeriay.women_articles_dict.values()
                          )

        # logger.info('\n'.join(map(str, self.result_tdvaleriay_women)))

    def run_men_parsing(self):
        for men_url in ConfigTDValeriay.men_urls:
            for url in men_url:
                text = self.load_page(url=url)
                self.parse_page(text=text)

        logger.info(f'Got {len(self.parsing_result)} elements MEN category')

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_tdvaleriay_men,
                          article_data=ConfigTDValeriay.men_articles_dict.values()
                          )

        # logger.info('\n'.join(map(str, self.result_tdvaleriay_men)))

    def run_children_parsing(self):
        for women_url in ConfigTDValeriay.children_urls:
            for url in women_url:
                text = self.load_page(url=url)
                self.parse_page(text=text)

        logger.info(f'Got {len(self.parsing_result)} elements CHILDREN category')

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_tdvaleriay_children,
                          article_data=ConfigTDValeriay.children_articles_dict.values())

        # logger.info('\n'.join(map(str, self.result_tdvaleriay_children)))


