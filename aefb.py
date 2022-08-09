from dataclasses import dataclass
from typing import Any


@dataclass
class general_data:
    td_elena_goods_name: Any = ''
    td_elena_article: Any = ''
    td_elena_price: Any = ''
    nataly_articles: Any = ''
    nataly_prices: Any = ''
    nataly_links: Any = ''
    gomany_articles: Any = ''
    gomany_prices: Any = ''
    gomany_links: Any = ''


data = general_data()
if data.gomany_articles:
    print('ojenviownjoweinsdfvgewrv')

import collections

company = 'TD_Elena'

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
    )
)
some = (ParseResult(
    goods_name="name,",
    article="article,",
    price="price,",
    sizes="sizes,",
    url="link,",
))
for i in some:
    print(i)

print(type(some))

if 'TD_Elena' in some.__class__.__name__:
    print("True 'TD_Elena'")

a = ''

if a:
    print('True')
