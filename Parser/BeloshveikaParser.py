import logging
import collections
import bs4
import requests
from Parser import config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Beloshveika')

product_category_name = '------'
ParseResult = collections.namedtuple(
    product_category_name,
    (
        'url',
        'goods_name',
        'price',
        'size'
    ),
)
