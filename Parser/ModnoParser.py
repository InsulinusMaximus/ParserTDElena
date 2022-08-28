import logging
import collections
import bs4
import requests
import Parser.Config.ModnoConfig as ConfigModno
from Parser.ArticlesFilter import article_filtering

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Modno')

company = 'MODNO'

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


class Parser_Modno:

    def __init__(self):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/101.0.4951.67 Safari/537.36'
        }
        # The main return write_list that contains named tuples with product data
        self.parsing_result = []
        self.result_modno_women = []
        self.result_modno_men = []
        self.result_modno_children = []

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

        try:
            title = product_title.select_one('a')
            link = 'https://modno-trikotazh.ru' + title.get('href')
        except AttributeError:
            link = '-'

        try:
            title = product_title.select_one('a')
            name = title.select_one('span.title').get_text().strip()
        except AttributeError:
            name = '-'

        article = name

        try:
            content = block.select_one('div.item_content')
            price = content.select_one('span.cennik').get_text().strip().replace('от ', '').replace(' ₽', '')
            price = price.replace(' ', '')
        except AttributeError:
            price = '-'

        try:
            content = block.select_one('div.item_content')
            chars = content.select_one('div.chars')
            sizes_container = chars.select_one('span.chars___filter_size_test')
            sizes = sizes_container.select_one('span.chars_char_data').get_text().strip().split(', ')
        except AttributeError:
            sizes = ['-']

        # Passing all variables, data store parsing individual elements, variable result (named tuple)
        self.parsing_result.append(ParseResult(
            goods_name=name,
            article=article,
            price=price,
            sizes=sizes,
            url=link,
        ))

    def run_women_parsing(self):
        for women_url in ConfigModno.women_urls:
            for url in women_url:
                logger.info(url)
                text = self.load_page(url=url)
                self.parse_page(text=text)

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_modno_women,
                          article_data=ConfigModno.women_articles_dict.values()
                          )

        logger.info('\n'.join(map(str, self.result_modno_women)))
        logger.info(f'Got {len(self.result_modno_women)} elements')

    def run_men_parsing(self):
        for men_url in ConfigModno.men_urls:
            for url in men_url:
                logger.info(url)
                text = self.load_page(url=url)
                self.parse_page(text=text)

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_modno_men,
                          article_data=ConfigModno.men_articles_dict.values()
                          )

        logger.info('\n'.join(map(str, self.result_modno_men)))
        logger.info(f'Got {len(self.result_modno_men)} elements')

    def run_children_parsing(self):
        for women_url in ConfigModno.children_urls:
            for url in women_url:
                text = self.load_page(url=url)
                self.parse_page(text=text)

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_modno_children,
                          article_data=ConfigModno.children_articles_dict.values())

        logger.info('\n'.join(map(str, self.result_modno_children)))
        logger.info(f'Got {len(self.result_modno_children)} elements')
