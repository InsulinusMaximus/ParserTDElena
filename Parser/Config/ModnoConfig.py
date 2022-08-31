# coding: utf-8
import collections

# Modno
# Women's LINKS

product_category_name = 'Women'
category_url = collections.namedtuple(
    product_category_name,
    (
        'halaty_toplyye',
        'halaty_logkiye',
        'platya',
        'sorochki_sitcevie',
        'sorochki',
        'sarafan',
        'pizhamy_s_bryukamy',
        'pizhamy_s_shortamy',
        'penyuary',
        'tuniky',
        'tolstovki',
        'kostyumy_s_bryukamy',
        'kostyumy_s_shortamy',
        'futbolky',
        'bryuki_bridzhi_shorty_yubki',
    )
)

halaty_toplyye = tuple('https://modno-trikotazh.ru/halaty-tyoplye/page=' + str(i) for i in range(1, 6))
halaty_logkiye = tuple('https://modno-trikotazh.ru/halaty-lyogkie/page=' + str(i) for i in range(1, 20))
platya = tuple('https://modno-trikotazh.ru/platja/page=36' + str(i) for i in range(1, 36))
sorochki_sitcevie = ('https://modno-trikotazh.ru/sorochki-sitcevye',)
sorochki = tuple('https://modno-trikotazh.ru/sorochki-trikotazhnye/page=' + str(i) for i in range(1, 16))
sarafan = tuple('https://modno-trikotazh.ru/platja-5bd19004a328b/page=' + str(i) for i in range(1, 10))
pizhamy_s_bryukamy = tuple('https://modno-trikotazh.ru/pizhamy-s-bryukami/page=' + str(i) for i in range(1, 9))
pizhamy_s_shortamy = tuple('https://modno-trikotazh.ru/pizhamy/page=' + str(i) for i in range(1, 10))
penyuary = tuple('https://modno-trikotazh.ru/komplekty/page=4' + str(i) for i in range(1, 5))
tuniky = tuple('https://modno-trikotazh.ru/tuniki/page=' + str(i) for i in range(1, 34))
tolstovki = tuple('https://modno-trikotazh.ru/tuniki/page=' + str(i) for i in range(1, 34))
kostyumy_s_bryukamy = tuple('https://modno-trikotazh.ru/kostyumy-s-bryukami/page=' + str(i) for i in range(1, 34))
kostyumy_s_shortamy = tuple('https://modno-trikotazh.ru/kostyumy/page=' + str(i) for i in range(1, 24))
futbolky = tuple('https://modno-trikotazh.ru/futbolki-maiki/page=' + str(i) for i in range(1, 24))
bryuki_bridzhi_shorty_yubki = tuple('https://modno-trikotazh.ru/shorty-bridzhi/page=' + str(i) for i in range(1, 16))


women_urls = category_url(
    halaty_toplyye=halaty_toplyye,
    halaty_logkiye=halaty_logkiye,
    platya=platya,
    sorochki_sitcevie=sorochki_sitcevie,
    sorochki=sorochki,
    sarafan=sarafan,
    pizhamy_s_bryukamy=pizhamy_s_bryukamy,
    pizhamy_s_shortamy=pizhamy_s_shortamy,
    penyuary=penyuary,
    tuniky=tuniky,
    tolstovki=tolstovki,
    kostyumy_s_bryukamy=kostyumy_s_bryukamy,
    kostyumy_s_shortamy=kostyumy_s_shortamy,
    futbolky=futbolky,
    bryuki_bridzhi_shorty_yubki=bryuki_bridzhi_shorty_yubki
    )

# Articles (SKU) are stored using the "Dictionary" data structure, since it is necessary to store data in the form -
# {key: value},
# since each Elena TD article must have a pair (pairs) for comparison.
# Storage is in the form of {key: (value,)}, since data tuples can act as values

# Women's ARTICLES (SKU)

women_articles_dict = {
    '321106': 'Футболка М-622 D',
    '319193': 'Сарафан 38109',
    '30047': 'Майка Р73 "Эмма"',
    '319172': 'Майка Р73 бретель',
    '31881': 'Майка СТ Пуговка',
    '321159а': 'Халат Т9 "Очарование"',
    '315160': 'Водолазка П3095/М-157',
    '319171': 'Водолазка Тея Б',
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

muzhskaya_domashnyaya_odezhda = tuple('https://modno-trikotazh.ru/men/page=' + str(i) for i in range(1, 24))

men_urls = category_url(
    muzhskaya_domashnyaya_odezhda=muzhskaya_domashnyaya_odezhda
    )

# Articles (SKU) are stored using the "Dictionary" data structure, since it is necessary to store data in the form -
# {key: value},
# since each Elena TD article must have a pair (pairs) for comparison.
# Storage is in the form of {key: (value,)}, since data tuples can act as values

# Men's ARTICLES (SKU)

men_articles_dict = {
    '10006': 'Футболка 32035',
    '12009Па': 'Пижама муж 4Н "Крокодильчики"',
    '10001': 'Майка 16629',
    '11932': 'Халат Т9 "Честер"',
    '11528ВШ': 'Халат 9-119 НК',
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

