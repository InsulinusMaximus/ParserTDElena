import logging
import collections
import bs4
import requests
from Parser import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Natali')

# To write the parsed data of one card, the data type is used - a named tuple
product_category_name = 'Футболки'
ParseResult = collections.namedtuple(
    product_category_name,
    (
        'url',
        'goods_name',
        'price',
        'size'
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
        # The main return list that contains named tuples with product data
        self.result = []

    # Method that loads a page and returns HTML in a text format
    def load_page(self, url):
        try:
            res = self.session.get(url=url)
            res.raise_for_status()
        except:
            print('Error')
        return res.text

    # Bringing the text of the downloaded page to BeautyfulSoup
    # Splitting the page into blocks (cards of a single product)
    def parse_page(self, text: str):
        soup = bs4.BeautifulSoup(text, 'lxml')
        container = soup.select('li.product-card.product-card--with-overlay')
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
        link = link_name_article.get('href')
        if not link:
            logger.error('No link')
            return
        link = 'https://natali37.ru/' + link
        # 5 lvl. Take out the name and article from the tag <a
        name = link_name_article.get_text()
        if not name:
            logger.error('No name')
            return
        name = name.split()

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
                purchasesize = '--'
            # 6 lvl. Saving the price, as well as catching an error in the absence of a price
            try:
                price = price_purchasesize.find('div', class_='price-table__value').text.strip()
            except AttributeError:
                price = '--'

            prices.update({purchasesize: price})

        # 3 lvl. 'sizes_productcard' gets all content related to dimensions
        sizes_productcard = content.select_one('div.sizes.product-card__sizes')
        if not sizes_productcard:
            logger.error('No sizes table')
            return
        # 4 lvl. Getting all sizes and saving to a list
        sizes = sizes_productcard.select_one('ul.sizes__list.list').get_text()
        if not sizes:
            logger.error('No sizes')
            return
        sizes = " ".join(sizes.split()).split()

        # Passing all variables, data store parsing individual elements, variable result (named tuple)
        self.result.append(ParseResult(
            url=link,
            goods_name=name,
            price=prices,
            size=sizes
        ))

    def run(self):
        for url in config.NatalyFutbolka:
            text = self.load_page(url=url)
            self.parse_page(text=text)
            logger.info(f'Got {len(self.result)} elements')

