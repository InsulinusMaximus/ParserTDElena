# coding: utf-8
import collections

# Gomany
# Women's LINKS
product_category_name = 'Women'
category_url = collections.namedtuple(
    product_category_name,
    (
        'zhenskaya_odezhda'
    )
)

zhenskaya_odezhda = tuple(f'https://gomani.ru/product-category/womens/page/' + str(i) for i in range(1, 4))

women_urls = category_url(
    zhenskaya_odezhda=zhenskaya_odezhda,
    )

# Articles (SKU) are stored using the "Dictionary" data structure, since it is necessary to store data in the form -
# {key: value},
# since each Elena TD article must have a pair (pairs) for comparison.
# Storage is in the form of {key: (value,)}, since data tuples can act as values

# Women's ARTICLES (SKU)

women_articles_dict = {
    '30081В': ('С792',),
    '30078Х': ('С787К',),
    '31468К': ('С866',),
    '30119': ('С1329',),
    '31437': ('С1311',),
    '32268': ('С1283',),
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

muzhskaya_domashnyaya_odezhda = ('https://gomani.ru/product-category/mens/',)


men_urls = category_url(
    muzhskaya_domashnyaya_odezhda=muzhskaya_domashnyaya_odezhda
    )

men_articles_dict = {
    '10256К': ('С677-2',),
    '10006': ('С677-1',),
    '10131': ('С143К',),
    '11725': ('С779',),
    '10022': ('С1156',),
    '11716': ('С152-1',),
}


# ____________________________________________________________________________________________________________________
# Children's LINKS

product_category_name = 'Children'
category_url = collections.namedtuple(
    product_category_name,
    (

    )
)

kostyumy = tuple('' + str(i) for i in range(1, 7))


children_urls = category_url(

)

# Articles (SKU) are stored using the "Dictionary" data structure, since it is necessary to store data in the form -
# {key: value},
# since each Elena TD article must have a pair (pairs) for comparison.
# Storage is in the form of {key: (value,)}, since data tuples can act as values

# Children ARTICLES (SKU)

children_articles_dict = {
}



