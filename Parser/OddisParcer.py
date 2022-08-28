import logging
import collections
import bs4
import requests
import Parser.Config.OddisConfig as ConfigOddis
from Parser.ArticlesFilter import article_filtering

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Oddis')

company = 'ODDIS'

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


class Parser_Oddis:

    def __init__(self):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        # The main return write_list that contains named tuples with product data
        self.parsing_result = []
        self.result_oddis_women = []
        self.result_oddis_men = []
        self.result_oddis_children = []

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
        all_cards = soup.select_one('ul.cat_ul')
        container = all_cards.select('li')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        product_title = block.select_one('div.catalog-capt')
        try:
            link = 'https://oddis.ru' + product_title.select_one('a').get('href')
        except AttributeError:
            link = '-'
        try:
            name = product_title.select_one('a').get_text().strip()
        except AttributeError:
            name = '-'

        try:
            article = block.select_one('div.catalog-art').get_text().replace('АРТ. ', '')
        except AttributeError:
            article = '-'

        try:
            price = block.select_one('div.catalog-price').get_text().replace('цена в розницу', '')
            price = price.replace('₽', '').split('-')
        except AttributeError:
            price = ['-']

        try:
            sizes = block.select_one('div.catalog-size').get_text().replace('Размер: ', '').split('-')
            if type(sizes) is list and len(sizes) >= 2:
                size = [i + 2 for i in range(int(sizes[0]), int(sizes[1]) - 1)]
            else:
                size = [sizes]
        except AttributeError:
            size = ['-']

        # Passing all variables, data store parsing individual elements, variable result (named tuple)
        self.parsing_result.append(ParseResult(
            goods_name=name,
            article=article,
            price=price,
            sizes=size,
            url=link,
        ))

    def run_women_parsing(self):
        for women_url in ConfigOddis.women_urls:
            for url in women_url:
                logger.info(url)
                text = self.load_page(url=url)
                self.parse_page(text=text)

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_oddis_women,
                          article_data=ConfigOddis.women_articles_dict.values()
                          )

        logger.info('\n'.join(map(str, self.result_oddis_women)))
        logger.info(f'Got {len(self.result_oddis_women)} elements')

    def run_men_parsing(self):
        for men_url in ConfigOddis.men_urls:
            for url in men_url:
                logger.info(url)
                text = self.load_page(url=url)
                self.parse_page(text=text)

        logger.info('\n'.join(map(str, self.parsing_result)))

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_oddis_men,
                          article_data=ConfigOddis.men_articles_dict.values()
                          )

        logger.info('\n'.join(map(str, self.result_oddis_men)))
        logger.info(f'Got {len(self.result_oddis_men)} elements')

    def run_children_parsing(self):
        for women_url in ConfigOddis.children_urls:
            for url in women_url:
                text = self.load_page(url=url)
                self.parse_page(text=text)

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_oddis_children,
                          article_data=ConfigOddis.children_articles_dict.values())

        logger.info('\n'.join(map(str, self.result_oddis_children)))
        logger.info(f'Got {len(self.result_oddis_children)} elements')
