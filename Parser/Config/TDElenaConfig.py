import collections

# TD Elena
# Women
product_category_name = 'Women'
category_url = collections.namedtuple(
    product_category_name,
    (
        'yubki',
        'tuniky',
        'platya',
        'sarafan',
        'zhilety',
        'bluzony',
        'belye',
        'sportivnyye_kostyumy',
        'halaty',
        'kapri',
        'futbolky',
        'topy',
        'vodolazki',
        'mayki',
        'dzhempery',
        'rubashki',
        'tolstovki',
        'sorochki',
        'pizhamy',
        'shorty',
        'bryuki',
        'bridzhi',
        'losiny',
        'velosipedki',
        'kostyumy_domashniye'
    )
)

yubki = ('https://td-elena.ru/catalog/zhenskaya_odezhda/yubki_1/',)
tuniky = tuple('https://td-elena.ru/catalog/zhenskaya_odezhda/tuniki/?PAGEN_1=' + str(i) for i in range(1, 3))
platya = tuple('https://td-elena.ru/catalog/zhenskaya_odezhda/plate/?PAGEN_1=' + str(i) for i in range(1, 8))
sarafan = tuple('https://td-elena.ru/catalog/zhenskaya_odezhda/sarafany/?PAGEN_1=' + str(i) for i in range(1, 3))
zhilety = ('https://td-elena.ru/catalog/zhenskaya_odezhda/zhilety/',)
bluzony = tuple('https://td-elena.ru/catalog/zhenskaya_odezhda/bluzony/?PAGEN_1=' + str(i) for i in range(1, 3))
belye = ('https://td-elena.ru/catalog/zhenskaya_odezhda/bele_1/',)
sportivnyye_kostyumy = tuple(
    'https://td-elena.ru/catalog/zhenskaya_odezhda/kostyumy_sportivnye/?PAGEN_1=' + str(i) for i in range(1, 4)
    )
halaty = tuple('https://td-elena.ru/catalog/zhenskaya_odezhda/khalaty_1/?PAGEN_1=' + str(i) for i in range(1, 7))
kapri = ('https://td-elena.ru/catalog/zhenskaya_odezhda/kapri/',)
futbolky = tuple('https://td-elena.ru/catalog/zhenskaya_odezhda/futbolki/?PAGEN_1=' + str(i) for i in range(1, 6))
topy = ('https://td-elena.ru/catalog/zhenskaya_odezhda/topy/?PAGEN_1=',)
vodolazki = ('https://td-elena.ru/catalog/zhenskaya_odezhda/vodolazki_1/?PAGEN_1=',)
mayki = ('https://td-elena.ru/catalog/zhenskaya_odezhda/mayki/?PAGEN_1=',)
dzhempery = tuple('https://td-elena.ru/catalog/zhenskaya_odezhda/dzhempery/?PAGEN_1=' + str(i) for i in range(1, 3))
rubashki = ('https://td-elena.ru/catalog/zhenskaya_odezhda/rubashki/?PAGEN_1=',)
tolstovki = tuple('https://td-elena.ru/catalog/zhenskaya_odezhda/tolstovki/?PAGEN_1=' + str(i) for i in range(1, 4))
sorochki = tuple('https://td-elena.ru/catalog/zhenskaya_odezhda/sorochki_1/?PAGEN_1=' + str(i) for i in range(1, 5))
pizhamy = tuple(
    'https://td-elena.ru/catalog/zhenskaya_odezhda/pizhamy_komplekty_/?PAGEN_1=' + str(i) for i in range(1, 5)
    )
shorty = tuple('https://td-elena.ru/catalog/zhenskaya_odezhda/shorty_1/?PAGEN_1=' + str(i) for i in range(1, 3))
bryuki = tuple('https://td-elena.ru/catalog/zhenskaya_odezhda/bryuki/?PAGEN_1=' + str(i) for i in range(1, 4))
bridzhi = ('https://td-elena.ru/catalog/zhenskaya_odezhda/bridzhi/?PAGEN_1=',)
losiny = ('https://td-elena.ru/catalog/zhenskaya_odezhda/losiny/?PAGEN_1=',)
velosipedki = ('https://td-elena.ru/catalog/zhenskaya_odezhda/velosipedki/?PAGEN_1=',)
kostyumy_domashniye = tuple(
    'https://td-elena.ru/catalog/zhenskaya_odezhda/kostyumy_domashnie_1/?PAGEN_1=' + str(i) for i in range(1, 6)
    )


women_urls = category_url(
    yubki=yubki,
    tuniky=tuniky,
    platya=platya,
    sarafan=sarafan,
    zhilety=zhilety,
    bluzony=bluzony,
    belye=belye,
    sportivnyye_kostyumy=sportivnyye_kostyumy,
    halaty=halaty,
    kapri=kapri,
    futbolky=futbolky,
    topy=topy,
    vodolazki=vodolazki,
    mayki=mayki,
    dzhempery=dzhempery,
    rubashki=rubashki,
    tolstovki=tolstovki,
    sorochki=sorochki,
    pizhamy=pizhamy,
    shorty=shorty,
    bryuki=bryuki,
    bridzhi=bridzhi,
    losiny=losiny,
    velosipedki=velosipedki,
    kostyumy_domashniye=kostyumy_domashniye
)

# ___________________________________________________________________________________________________________________

# Men
product_category_name = 'Men'
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

men_urls = category_url(
    kostyumy=kostyumy,
    futbolky=futbolky,
    tolstovki=tolstovki,
    bryuki=bryuki,
    halaty=halaty,
    shorty=shorty,
    pizhamy=pizhamy,
    kurtki=kurtki,
    )

# ___________________________________________________________________________________________________________________

# Children

product_category_name = 'Children'
category_url = collections.namedtuple(
    product_category_name,
    (
        'tolstovki',
        'kostyumy',
        'futbolky',

        'bryuki',
        'halaty',
        'shorty',
        'pizhamy',
        'kurtki',
    )
)

tolstovki = tuple('https://td-elena.ru/catalog/detskaya_odezhda/zhiletki_tolstovki/?PAGEN_1=2' + str(i) for i in range(1, 8))

kostyumy = tuple('https://natali37.ru/catalog/category/210?page=' + str(i) for i in range(1, 7))
futbolky = tuple('https://natali37.ru/catalog/category/213?page=' + str(i) for i in range(1, 22))

bryuki = tuple('https://natali37.ru/catalog/category/217?page=' + str(i) for i in range(1, 6))
halaty = ('https://natali37.ru/catalog/category/220?page=1',)
shorty = tuple('https://natali37.ru/catalog/category/219?page=' + str(i) for i in range(1, 5))
pizhamy = ('https://natali37.ru/catalog/category/314?page=',)
kurtki = ('https://natali37.ru/catalog/category/581?page=',)

children_urls = category_url(
    kostyumy=kostyumy,
    futbolky=futbolky,
    tolstovki=tolstovki,
    bryuki=bryuki,
    halaty=halaty,
    shorty=shorty,
    pizhamy=pizhamy,
    kurtki=kurtki,
    )
