import logging
import collections
import bs4
import requests
import Parser.Config.GomanyConfig as ConfigGomany
from Parser.ArticlesFilter import article_filtering

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Gomany')

company = 'GOMANY'

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


class Parser_Gomany:

    def __init__(self):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        # The main return list that contains named tuples with product data
        self.parsing_result = []
        self.result_gomany_women = []
        self.result_gomany_men = []
        self.result_gomany_children = []

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
            prices = block.select_one('span.prices').get_text().strip().replace('₽', '').replace(',', '').split(' – ')
        except AttributeError:
            prices = ['-']

        try:
            sizes = block.select_one('div.sku').get_text().replace('Размеры: ', '').split(', ')
        except AttributeError:
            sizes = ['-']

        # Passing all variables, data store parsing individual elements, variable result (named tuple)
        self.parsing_result.append(ParseResult(
            goods_name=name,
            article=article,
            price=prices,
            sizes=sizes,
            url=link
        ))

    def run_women_parsing(self):
        for women_url in ConfigGomany.women_urls:
            for url in women_url:
                logger.info(url)
                text = self.load_page(url=url)
                self.parse_page(text=text)

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_gomany_women,
                          article_data=ConfigGomany.women_articles_dict.values()
                          )

        logger.info('\n'.join(map(str, self.result_gomany_women)))
        logger.info(f'Got {len(self.result_gomany_women)} elements')

    def run_men_parsing(self):
        for men_url in ConfigGomany.men_urls:
            for url in men_url:
                logger.info(url)
                text = self.load_page(url=url)
                self.parse_page(text=text)

        logger.info('\n'.join(map(str, self.parsing_result)))

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_gomany_men,
                          article_data=ConfigGomany.men_articles_dict.values()
                          )

        logger.info('\n'.join(map(str, self.result_gomany_men)))
        logger.info(f'Got {len(self.result_gomany_men)} elements')

    def run_children_parsing(self):
        for women_url in ConfigGomany.children_urls:
            for url in women_url:
                text = self.load_page(url=url)
                self.parse_page(text=text)

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_gomany_children,
                          article_data=ConfigGomany.children_articles_dict.values())

        logger.info('\n'.join(map(str, self.result_gomany_children)))
        logger.info(f'Got {len(self.result_gomany_children)} elements')


