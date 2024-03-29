import logging
import collections
import bs4
import requests
import Parser.Config.NatalyConfig as ConfigNataly
from Parser.ArticlesFilter import article_filtering

company = 'NATALY'

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


class Parser_Nataly:

    def __init__(self):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        # The main return write_list that contains named tuples with product data
        self.parsing_result = []
        self.result_nataly_women = []
        self.result_nataly_men = []
        self.result_nataly_children = []

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
            container = soup.select('li.product-card.product-card--with-overlay')
        except AttributeError:
            logger.info('There are no required attributes on the page')
            return None

        for block in container:
            self.parse_block(block=block)

    # Parsing of each block (cards of a single product)
    def parse_block(self, block):
        # 1 lvl. 'wrapper' is the entire contents of the block
        wrapper = block.select_one('div.product-card__wrapper')
        if not wrapper:
            logger.error('No product card wrapper')
            return
        # 2 lvl. 'content' is all content without photos and infographics
        content = wrapper.select_one('div.product-card__content')
        if not content:
            logger.error('No card content')
            return

        # 3 lvl. 'heading' contains the card name, article and link
        heading = content.select_one('div.product-card__heading')
        if not heading:
            logger.error('No card heading')
            return
        # 4 lvl. 'link_name_article' contains the href attribute with a link to the product card
        # and the name with the article
        link_name_article = heading.select_one('a.product-card__name.link')
        if not link_name_article:
            logger.error('No product card linc and name with article')
            return
        # 5 lvl. Get link from attribute href
        try:
            link = link_name_article.get('href')
        except AttributeError:
            link = None
        link = 'https://natali37.ru/' + link
        # 5 lvl. Take out the name and article from the tag <a
        try:
            name = link_name_article.get_text().strip()
        except AttributeError:
            name = '-'
        article_in_link = link.split('/')
        article = '0' + article_in_link[-1]
        # 3 lvl. 'pricetable_productcard' contains tags with price tables (purchase size - price)
        pricetable_productcard = content.select_one('div.price-table.product-card__price-table')
        if not pricetable_productcard:
            logger.error('No price table, product card')
            return
        # 4 lvl. Finding all columns of a table (purchase size - price)
        price_table = pricetable_productcard.find_all('div', class_='price-table__column')
        if not price_table:
            logger.error('No price table')
            return
        # Creating a dictionary to store key-value ("Purchase size": "Price")
        prices = {}
        # 5 lvl. Removing from each price_table the purchase size and price
        for price_purchasesize in price_table:
            # 6 lvl. Save purchase size name, and catch error if purchase size name is missing
            try:
                purchasesize = price_purchasesize.find('div', class_='price-table__name').text.strip()
            except AttributeError:
                purchasesize = '-'
            # 6 lvl. Saving the price, as well as catching an error in the absence of a price
            try:
                price = price_purchasesize.find('div', class_='price-table__value').text.replace('₽', '').strip()
                price = price.replace('\t', '').replace('\n', '')
            except AttributeError:
                price = '-'

            prices.update({purchasesize: price})

        # 3 lvl. 'sizes_productcard' gets all content related to dimensions
        sizes_productcard = content.select_one('div.sizes.product-card__sizes')
        if not sizes_productcard:
            logger.error('No sizes table')
            return
        # 4 lvl. Getting all sizes and saving to a write_list
        try:
            sizes = sizes_productcard.select_one('ul.sizes__list.write_list').get_text().split()
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
        for women_url in ConfigNataly.women_urls:
            for url in women_url:
                text = self.load_page(url=url)
                self.parse_page(text=text)

        logger.info(f'Got {len(self.parsing_result)} elements WOMEN category')

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_nataly_women,
                          article_data=ConfigNataly.women_articles_dict.values()
                          )

        # logger.info('\n'.join(map(str, self.result_nataly_women)))

    def run_men_parsing(self):
        for men_url in ConfigNataly.men_urls:
            for url in men_url:
                text = self.load_page(url=url)
                self.parse_page(text=text)

        logger.info(f'Got {len(self.parsing_result)} elements MEN category')

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_nataly_men,
                          article_data=ConfigNataly.men_articles_dict.values()
                          )

        # logger.info('\n'.join(map(str, self.result_nataly_men)))

    def run_children_parsing(self):
        for women_url in ConfigNataly.children_urls:
            for url in women_url:
                text = self.load_page(url=url)
                self.parse_page(text=text)

        logger.info(f'Got {len(self.parsing_result)} elements CHILDREN category')

        article_filtering(parsing_result=self.parsing_result,
                          category_result=self.result_nataly_children,
                          article_data=ConfigNataly.children_articles_dict.values())

        # logger.info('\n'.join(map(str, self.result_nataly_children)))

