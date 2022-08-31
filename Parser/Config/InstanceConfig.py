import collections

# Instance
# Women's LINKS

product_category_name = 'Women'
category_url = collections.namedtuple(
    product_category_name,
    (
        'tuniky',
        'losiny',
        'futbolky',
        'halaty',
        'kostyumy',
        'shorty',
        'dzhempery',
        'bryuki',
        'bridzhi',
        'pizhamy',
        'platya_sarafany',
        'sorochki',
        'tolstovki',
    )
)

tuniky = tuple('https://instanceshop.ru/tuniki/?page=' + str(i) for i in range(1, 3))
losiny = tuple('https://instanceshop.ru/losiny/?page=' + str(i) for i in range(1, 3))
futbolky = tuple('https://instanceshop.ru/futbolki/?page=' + str(i) for i in range(1, 7))
halaty = tuple('https://instanceshop.ru/halaty/?page=' + str(i) for i in range(1, 3))
kostyumy = tuple('https://instanceshop.ru/kostjumy/?page=' + str(i) for i in range(1, 6))
shorty = tuple('https://instanceshop.ru/shorty/?page=' + str(i) for i in range(1, 3))
dzhempery = tuple('https://instanceshop.ru/dzhempery/?page=' + str(i) for i in range(1, 6))
bryuki = tuple('https://instanceshop.ru/bryuki/?page=' + str(i) for i in range(1, 3))
bridzhi = ('https://instanceshop.ru/bridzhi/',)
pizhamy = tuple('https://instanceshop.ru/pizhamy/?page=' + str(i) for i in range(1, 3))
platya_sarafany = tuple('https://instanceshop.ru/platya-i-sarafany/?page=' + str(i) for i in range(1, 6))
sorochki = tuple('https://instanceshop.ru/nochnushki-i-sorochki/?page=' + str(i) for i in range(1, 3))
tolstovki = tuple('https://instanceshop.ru/kofty/?page=' + str(i) for i in range(1, 4))

women_urls = category_url(
    tuniky=tuniky,
    losiny=losiny,
    futbolky=futbolky,
    halaty=halaty,
    kostyumy=kostyumy,
    shorty=shorty,
    dzhempery=dzhempery,
    bryuki=bryuki,
    bridzhi=bridzhi,
    pizhamy=pizhamy,
    platya_sarafany=platya_sarafany,
    sorochki=sorochki,
    tolstovki=tolstovki
)

# Articles (SKU) are stored using the "Dictionary" data structure, since it is necessary to store data in the form -
# {key: value},
# since each Elena TD article must have a pair (pairs) for comparison.
# Storage is in the form of {key: (value,)}, since data tuples can act as values

# Women's ARTICLES (SKU)

women_articles_dict = {
    '30078': ('М-0063К',),
    '31468': ('М-0186БЕЖ',),
    '319172': ('М-0069ТС',),
    '30119': ('М-0010ТС',),
    '321159': ('М-0070З',),
    '30043': ('М-0042БЕЖ',),
    '32268': ('М-0011З',),
}

# ____________________________________________________________________________________________________________________
# Men's LINKS

product_category_name = 'Men'
category_url = collections.namedtuple(
    product_category_name,
    (
        'muzhskaya_odezhda',
    )
)

muzhskaya_odezhda = tuple('https://instanceshop.ru/muzhskaya-odezhda/?page=' + str(i) for i in range(1, 5))

men_urls = category_url(
    muzhskaya_odezhda=muzhskaya_odezhda
)

# Articles (SKU) are stored using the "Dictionary" data structure, since it is necessary to store data in the form -
# {key: value},
# since each Elena TD article must have a pair (pairs) for comparison.
# Storage is in the form of {key: (value,)}, since data tuples can act as values

# Men's ARTICLES (SKU)

men_articles_dict = {
    '11606': ('С-0007Ч',),
}

# ____________________________________________________________________________________________________________________
# Children's LINKS
product_category_name = 'Children'
category_url = collections.namedtuple(
    product_category_name,
    (
        'kostyumy',
        'futbolky',
        'tolstovki',
        'bryuki',
        'halaty',
        'shorty',
        'pizhamy',
        'kurtki',
    )
)

kostyumy = tuple('https://natali37.ru/catalog/category/210?page=' + str(i) for i in range(1, 7))
futbolky = tuple('https://natali37.ru/catalog/category/213?page=' + str(i) for i in range(1, 22))
tolstovki = tuple('https://natali37.ru/catalog/category/215?page=' + str(i) for i in range(1, 8))
bryuki = tuple('https://natali37.ru/catalog/category/217?page=' + str(i) for i in range(1, 6))
halaty = ('https://natali37.ru/catalog/category/220?page=1',)
shorty = tuple('https://natali37.ru/catalog/category/219?page=' + str(i) for i in range(1, 5))
pizhamy = ('https://natali37.ru/catalog/category/314?page=',)
kurtki = ('https://natali37.ru/catalog/category/581?page=',)

children_urls = category_url(
    kostyumy,
    futbolky,
    tolstovki,
    bryuki,
    halaty,
    shorty,
    pizhamy,
    kurtki,
)

# Articles (SKU) are stored using the "Dictionary" data structure, since it is necessary to store data in the form -
# {key: value},
# since each Elena TD article must have a pair (pairs) for comparison.
# Storage is in the form of {key: (value,)}, since data tuples can act as values

# Children ARTICLES (SKU)

children_articles_dict = {
}
