import logging
import collections
import bs4
import requests
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Instance')

# To write the parsed data of one card, the data type is used - a named tuple
product_category_name = 'Футболки'
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


class Parser_Instance:

    def __init__(self):
        # Create session object and pass request parameters
        self.session = requests.session()
        self.session.headers = {
            'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
            '(KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }
        # The main return write_list that contains named tuples with product data
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
        container = soup.select('div.product-layout')
        for block in container:
            self.parse_block(block=block)

    def parse_block(self, block):
        card_caption = block.select_one('div.caption')
        product_title = card_caption.select_one('a.dv-product-title')
        link = product_title.get('href')
        name = product_title.get_text().strip()

        # Getting data from the card page
        res_card_inside = self.load_page(link)
        soup_card_inside = bs4.BeautifulSoup(res_card_inside, 'lxml')

        # Parsing the article from the inner page of the card
        article = soup_card_inside.select_one('li.article-product').text
        article = re.sub(r'Артикул:', '', article).strip()
        # Deletion from the name of the article
        if article in name:
            name = name.replace(article, '').strip()
        # Parsing prices from the inner page of the card
        price_conteiner = soup_card_inside.select_one('ul.write_list-unstyled.price-container')
        try:
            price = price_conteiner.select_one('meta', itemprop="price").get('content')
        except AttributeError:
            price = price_conteiner.select_one('span.newprice').get_text().strip().replace(' руб.', '')
        # Parsing the size range from the inner page of the card
        sizes_container = soup_card_inside.select_one('div.form-group.required')
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
        self.result.append(ParseResult(
            url=link,
            goods_name=name,
            article=article,
            price=price,
            sizes=sizes
        ))

    def run(self):
        # for url in Config.NatalyFutbolka:
        text = self.load_page(url='https://instanceshop.ru/bridzhi/')
        self.parse_page(text=text)
        # for card_data in self.result:
        # logger.info(card_data)
        # logger.info(f'Got {len(self.result)} elements')


if __name__ == '__main__':
    parser = Parser_Instance()
    parser.run()

    for i in parser.result:
        print(i[1])
