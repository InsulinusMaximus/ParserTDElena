import logging
import collections
import bs4
import requests
import Parser.Config.TDElenaConfig as ConfigTDElena
import Parser.Config.NatalyConfig as ConfigNataly

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('TDElena')

company = 'TDElena'

# To write the parsed data of one card, the data type is used - a named tuple
product_category_name = 'All'
ParseResult = collections.namedtuple(
    product_category_name,
    (
        'company',
        'url',
        'goods_name',
        'article',
        'price',
        'sizes'
    ),
)


class Parser_TDElena:

    def __init__(self):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        # The main return list that contains named tuples with product data
        self.parsing_result = []
        self.result_tdelena_women = []
        self.result_tdelena_men = []
        self.result_tdelena_children = []

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
        soup = bs4.BeautifulSoup(text, 'html.parser')
        catalog_block = soup.select_one('div.catalog_block')
        container = catalog_block.select('div.catalog_item_wrapp')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        item_title = block.select_one('div.item-title')

        try:
            link = 'https://td-elena.ru' + item_title.select_one('a').get('href')
        except AttributeError:
            link = None

        # Getting data from the card page
        res_card_inside = self.load_page(link)
        soup_card_inside = bs4.BeautifulSoup(res_card_inside, 'lxml')

        # Parsing the name from the inner page of the card
        content = soup_card_inside.select_one('div.container')
        try:
            name = content.select_one('h1').get_text().strip()
        except AttributeError:
            name = '-'

        # Parsing the article from the inner page of the card
        article_block = content.select_one('div.article.iblock')
        try:
            article = article_block.select_one('span.value').get_text().strip()
            article = ''.join(filter(str.isdigit, article))
        except AttributeError:
            article = '-'

        # Parsing prices from the inner page of the card
        total_price = content.select_one('div.price.total_price')
        try:
            price = total_price.select_one('span.price-val').get_text().strip()
        except AttributeError:
            price = '-'

        # Parsing the size range from the inner page of the card
        size_table = content.select_one('tbody')
        sizes = {}
        try:
            size_table_rows = size_table.select('tr')
        except AttributeError:
            size_table_rows = None
            sizes.update({'-': '-'})

        if size_table_rows is not None:
            for size_table_row in size_table_rows:
                try:
                    size = size_table_row.select_one('td').get_text()
                except AttributeError:
                    size = '-'
                try:
                    size_price = size_table_row.select_one('td.store-price').get_text()
                except AttributeError:
                    size_price = '-'

                sizes.update({size: size_price})
            if 'Все размеры (размерный ряд)' in sizes:
                del sizes['Все размеры (размерный ряд)']

            # Passing all variables, data store parsing individual elements, variable result (named tuple)
            self.parsing_result.append(ParseResult(
                company=company,
                goods_name=name,
                article=article,
                price=price,
                sizes=sizes,
                url=link,
            ))

    def article_filtering(self, parsing_result, category_result, articles_data):
        for card_data in parsing_result:
            if card_data.article in articles_data:
                category_result.append(card_data)
                logger.info(f'Got {len(self.parsing_result)} elements')

    def run_women_parsing(self):
        for women_url in ConfigTDElena.women_urls:
            for url in women_url:
                logger.info(url)
                text = self.load_page(url=url)
                self.parse_page(text=text)

        self.article_filtering(parsing_result=self.parsing_result,
                               category_result=self.result_tdelena_women,
                               articles_data=ConfigNataly.articles_td_elena_women
                               )

        logger.info('\n'.join(map(str, self.result_tdelena_women)))
        logger.info(f'Got {len(self.result_tdelena_women)} elements')

    def run_men_parsing(self):
        for men_url in ConfigTDElena.men_urls:
            for url in men_url:
                text = self.load_page(url=url)
                self.parse_page(text=text)

        self.article_filtering(parsing_result=self.parsing_result,
                               category_result=self.result_tdelena_men,
                               articles_data=ConfigNataly.articles_td_elena_men
                               )

        logger.info('\n'.join(map(str, self.result_tdelena_men)))
        logger.info(f'Got {len(self.result_tdelena_men)} elements')

    def run_children_parsing(self):
        for women_url in ConfigTDElena.children_urls:
            for url in women_url:
                text = self.load_page(url=url)
                self.parse_page(text=text)

        self.article_filtering(parsing_result=self.parsing_result,
                               category_result=self.result_tdelena_children,
                               articles_data=ConfigNataly.articles_td_elena_children)

        logger.info('\n'.join(map(str, self.result_tdelena_children)))
        logger.info(f'Got {len(self.result_tdelena_children)} elements')





