import collections

# Gomany
# Women
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

women_articles_dict = {
    '30081В': 'С792',
    '30078Х': 'С787К',
    '31468К': 'С866',
    '30119': 'С1329',
    '31437': 'С1311',
    '32268': 'С1283',
}

# ____________________________________________________________________________________________________________________
# Men
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
    '10256': 'С677-2',
    '10006': 'С677-1',
    '10131': 'С143К',
    '11725': 'С779',
    '10022': 'С1156',
    '11716': 'С152-1',
}


# ____________________________________________________________________________________________________________________
# Children
product_category_name = 'Children'
category_url = collections.namedtuple(
    product_category_name,
    (

    )
)

kostyumy = tuple('' + str(i) for i in range(1, 7))


children_urls = category_url(

)

children_articles_dict = {
}



