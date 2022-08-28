import logging
import collections
import bs4
import requests
import Parser.Config.InstanceConfig as ConfigInstance
from Parser.ArticlesFilter import article_filtering

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Instance')

company = 'INSTANCE'

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


class Parser_Instance:

    def __init__(self):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        # The main return write_list that contains named tuples with product data
        self.parsing_result = []
        self.result_instance_women = []
        self.result_instance_men = []
        self.result_instance_children = []

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
        catalog = soup.select_one('div.bbry-catalog__list')
        container = catalog.select('div.bbry-product-card')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        try:
            title = block.select_one('a')
            link = title.get('href').strip()
            name = title.get_text().strip()
        except AttributeError:
            link = '-'
            name = '-'

        # Parsing the article from the inner page of the card
        card_body = block.select_one('div.bbry-product-card__body')

        try:
            article_container = card_body.select_one('div.bbry-product-card__vendor-code')
            article = article_container.select_one('span.vendor-code__value').get_text().strip()
        except AttributeError:
            article = '-'

        try:
            price_container = card_body.select_one('div.bbry-product-card__price')
            price = price_container.select_one('span').get_text().strip().replace(' руб.', '')
        except AttributeError:
            price = '-'

        # Getting data from the card page
        card_inside = self.load_page(link)
        soup_card_inside = bs4.BeautifulSoup(card_inside, 'lxml')

        # Parsing the size range from the inner page of the card
        sizes_container = soup_card_inside.select_one('div.txt-block__filters')
        sizes_group = sizes_container.select('option')
        sizes = []
        for size in sizes_group:
            size = size.get_text().strip()
            # I check for the absence of any characters other than numbers,
            # since the first parsed field would always be "---Enter---"
            size_num = size.isdigit()
            if size_num is True:
                sizes.append(size)

        # Passing all variables, data store parsing individual elements, variable result (named tuple)
        self.parsing_result.append(ParseResult(
            goods_name=name,
            article=article,
            price=price,
            sizes=sizes,
            url=link,
        ))

    def run_women_parsing(self):
        for women_url in ConfigInstance.women_urls:
            for url in women_url:
                logger.info(url)
                text = self.load_page(url=url)
                self.parse_page(text=text)

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_instance_women,
                          article_data=ConfigInstance.women_articles_dict.values()
                          )

        logger.info('\n'.join(map(str, self.result_instance_women)))
        logger.info(f'Got {len(self.result_instance_women)} elements')

    def run_men_parsing(self):
        for men_url in ConfigInstance.men_urls:
            for url in men_url:
                logger.info(url)
                text = self.load_page(url=url)
                self.parse_page(text=text)

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_instance_men,
                          article_data=ConfigInstance.men_articles_dict.values()
                          )

        logger.info('\n'.join(map(str, self.result_instance_men)))
        logger.info(f'Got {len(self.result_instance_men)} elements')

    def run_children_parsing(self):
        for women_url in ConfigInstance.children_urls:
            for url in women_url:
                text = self.load_page(url=url)
                self.parse_page(text=text)

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_instance_children,
                          article_data=ConfigInstance.children_articles_dict.values())

        logger.info('\n'.join(map(str, self.result_instance_children)))
        logger.info(f'Got {len(self.result_instance_children)} elements')
