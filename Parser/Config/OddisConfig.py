import collections

# Oddis
# Women's LINKS
product_category_name = 'Women'
category_url = collections.namedtuple(
    product_category_name,
    (
        'zhenskaya_odezhda'
    )
)

zhenskaya_odezhda = tuple(f'https://oddis.ru/produkciya/zhenshchinam/str-' + str(i) for i in range(1, 22))

women_urls = category_url(
    zhenskaya_odezhda=zhenskaya_odezhda,
)

# Articles (SKU) are stored using the "Dictionary" data structure, since it is necessary to store data in the form -
# {key: value},
# since each Elena TD article must have a pair (pairs) for comparison.
# Storage is in the form of {key: (value,)}, since data tuples can act as values

# Women's ARTICLES (SKU)

women_articles_dict = {
    '30116': ('9.1314',),
}

# ____________________________________________________________________________________________________________________
# Men's LINKS

product_category_name = 'Men'
category_url = collections.namedtuple(
    product_category_name,
    (
        'muzhskaya_domashnyaya_odezhda',
    )
)

muzhskaya_domashnyaya_odezhda = tuple(f'https://oddis.ru/produkciya/muzhchinam/str-' + str(i) for i in range(1, 3))

men_urls = category_url(
    muzhskaya_domashnyaya_odezhda=muzhskaya_domashnyaya_odezhda
)

men_articles_dict = {
    '12107': ('5.176.1',),
}

# ____________________________________________________________________________________________________________________
# Children's LINKS

product_category_name = 'Children'
category_url = collections.namedtuple(
    product_category_name,
    (
        'detskaya_odezhda',
    )
)

detskaya_odezhda = tuple(f'https://oddis.ru/produkciya/detyam/str-' + str(i) for i in range(1, 3))

children_urls = category_url(
    detskaya_odezhda=detskaya_odezhda
)

# Articles (SKU) are stored using the "Dictionary" data structure, since it is necessary to store data in the form -
# {key: value},
# since each Elena TD article must have a pair (pairs) for comparison.
# Storage is in the form of {key: (value,)}, since data tuples can act as values

# Children ARTICLES (SKU)

children_articles_dict = {
    '21563И': ('1.1104',),
    '21421М': ('1.075.1',),
    '21436М': ('1.075.2',),
    '21827': ('1.1104',),
    '21452-Л': ('1.036',),
}
