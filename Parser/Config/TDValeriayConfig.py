import collections

# TD Valeriay
# Women's LINKS

product_category_name = 'Women'
category_url = collections.namedtuple(
    product_category_name,
    (
        'zhenskaya_odezhda'
    )
)

zhenskaya_odezhda = tuple('https://tdvaleria.ru/catalog/dlya_zhenshchin/?PAGEN_1=' + str(i) for i in range(1, 54))

women_urls = category_url(
    zhenskaya_odezhda=zhenskaya_odezhda,
    )

# Articles (SKU) are stored using the "Dictionary" data structure, since it is necessary to store data in the form -
# {key: value},
# since each Elena TD article must have a pair (pairs) for comparison.
# Storage is in the form of {key: (value,)}, since data tuples can act as values

# Women's ARTICLES (SKU)

women_articles_dict = {
    '31882': ('2/21-2230Фбр',),
    '30047': ('2/13-2120н',),
    '30071': ('2/14-2080а-',),
    '30119': ('2/14-2040г',),
    '30071О': ('2/13-2080о',),
    '319191': ('2/13-2240бв',),
    '30041А': ('2/13-2130н',),
    '315159Л': ('2/17-2200Ар',),
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

muzhskaya_domashnyaya_odezhda = tuple('https://tdvaleria.ru/catalog/dlya_muzhchin/?PAGEN_1=' + str(i) for i in range(1, 10))


men_urls = category_url(
    muzhskaya_domashnyaya_odezhda=muzhskaya_domashnyaya_odezhda
    )

# Articles (SKU) are stored using the "Dictionary" data structure, since it is necessary to store data in the form -
# {key: value},
# since each Elena TD article must have a pair (pairs) for comparison.
# Storage is in the form of {key: (value,)}, since data tuples can act as values

# Men's ARTICLES (SKU)

men_articles_dict = {
    '10256К': ('1/13-1130к',),
    '11606': ('1/13-1030н',),
    '10131': ('1/13-1030к',),
    '11725': ('1/16-1082С',),
    '10022': ('1/13-1020к',),
    '10002Б': ('1/13-1090н',),
    '10002К': ('1/13-1090к',),
    '11607А': ('1/13-1110ш',),
    '10004Х': ('1/13-1120х',),
    '11607': ('1/13-1110х',),
}


# ____________________________________________________________________________________________________________________
# Children's LINKS
product_category_name = 'Children'
category_url = collections.namedtuple(
    product_category_name,
    (

    )
)

kostyumy = tuple('https://natali37.ru/catalog/category/210?page=' + str(i) for i in range(1, 7))


children_urls = category_url(

    )

# Articles (SKU) are stored using the "Dictionary" data structure, since it is necessary to store data in the form -
# {key: value},
# since each Elena TD article must have a pair (pairs) for comparison.
# Storage is in the form of {key: (value,)}, since data tuples can act as values

# Children ARTICLES (SKU)

children_articles_dict = {
}

