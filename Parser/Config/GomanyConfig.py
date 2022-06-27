import collections

# TDElena
# Women
product_category_name = 'Women'
category_url = collections.namedtuple(
    product_category_name,
    (
        'womens_clothing'
    )
)

womens_clothing = tuple('https://gomani.ru/product-category/womens/page/' + str(i) for i in range(1, 4))


women_urls = category_url(
    womens_clothing=womens_clothing
    )

# Articles

category = 'Women'
articles = collections.namedtuple(
    category,
    (
        'TD_Elena',
        'Gomany'
    )
)

articles_gomany = (
    'С792',
    'С787К',
    'С866',
    'С1329',
    'С1311',
    'С1283'
)

articles_td_elena = (
    '30081В',
    '30078Х',
    '31468К',
    '30119',
    '31437',
    '32268'
)

women_articles = articles(
    TD_Elena=articles_td_elena,
    Gomany=articles_gomany
)

# ____________________________________________________________________________________________________________________
# Men




