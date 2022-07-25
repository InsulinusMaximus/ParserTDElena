import collections

# Nataly
# Women
product_category_name = 'Women'
category_url = collections.namedtuple(
    product_category_name,
    (
        'halaty',
        'tuniky',
        'sarafan',
        'platya',
        'kostyumy',
        'sorochki',
        'penyuary',
        'pizhamy',
        'futbolky',
        'tolstovki',
        'zhakety',
        'kurtki',
        'bryuki',
        'bridzhi',
        'shorty',
        'yubki',
        'sportivnaya_odezhda'
    )
)

halaty = tuple('https://natali37.ru/catalog/category/163?page=' + str(i) for i in range(1, 30))
tuniky = tuple('https://natali37.ru/catalog/category/164?page=' + str(i) for i in range(1, 44))
sarafan = tuple('https://natali37.ru/catalog/category/165?page=' + str(i) for i in range(1, 9))
platya = tuple('https://natali37.ru/catalog/category/166?page=' + str(i) for i in range(1, 34))
kostyumy = tuple('https://natali37.ru/catalog/category/167?page=' + str(i) for i in range(1, 63))
sorochki = tuple('https://natali37.ru/catalog/category/171?page=' + str(i) for i in range(1, 24))
penyuary = tuple('https://natali37.ru/catalog/category/172?page=' + str(i) for i in range(1, 5))
pizhamy = tuple('https://natali37.ru/catalog/category/173?page=' + str(i) for i in range(1, 16))
futbolky = tuple('https://natali37.ru/catalog/category/174?page=' + str(i) for i in range(1, 25))
tolstovki = tuple('https://natali37.ru/catalog/category/177?page=' + str(i) for i in range(1, 14))
zhakety = tuple('https://natali37.ru/catalog/category/178?page=' + str(i) for i in range(1, 4))
kurtki = ('https://natali37.ru/catalog/category/179?page=',)
bryuki = tuple('https://natali37.ru/catalog/category/180?page=' + str(i) for i in range(1, 12))
bridzhi = tuple('https://natali37.ru/catalog/category/181?page=' + str(i) for i in range(1, 4))
shorty = tuple('https://natali37.ru/catalog/category/182?page=' + str(i) for i in range(1, 4))
yubki = tuple('https://natali37.ru/catalog/category/183?page=' + str(i) for i in range(1, 5))
sportivnaya_odezhda = tuple('https://natali37.ru/catalog/category/731?page=' + str(i) for i in range(1, 24))

women_urls = category_url(
    halaty=halaty,
    tuniky=tuniky,
    sarafan=sarafan,
    platya=platya,
    kostyumy=kostyumy,
    sorochki=sorochki,
    penyuary=penyuary,
    pizhamy=pizhamy,
    futbolky=futbolky,
    tolstovki=tolstovki,
    zhakety=zhakety,
    kurtki=kurtki,
    bryuki=bryuki,
    bridzhi=bridzhi,
    shorty=shorty,
    yubki=yubki,
    sportivnaya_odezhda=sportivnaya_odezhda
    )

women_articles_dict = {
    '32291': '025188',
    '31822': '011200',
    '31946': '08130',
    '31430': '055016',
    '322107': '025575',
    '31969': '015567',
    '322165': '032042',
    '322125': '08080',
    '321165': '026683',
    '31729': '027724',
    '32139': '025761',
    '320165': '024726',
    '30040': '03677',
    '315159': '012425',
    '31757': '021101',
    '31758': '015032',
    '32247': '025196',
    '32189': '024328',
    '32049': '017905',
    '32221': '024807',
    '32242': '012801',
    '32070': '024035',
    '32229': '025130',
    '320129': '025254',
    '320103': '020476',
    '322105': '025808',
    '32058': '05387',
    '32251': '01583',
    '32275': '08508',
    '32276': '024187',
    '32227': '026195',
    '32268': '025682',
    '32011': '04931',
    '32111': '025703',
    '321153': '023053',
    '32263': '018203',
    '322102': '024360',
    '31587': '09234',
    '320184': '05534',
    '31497': '021844',
    '319216': '020550',
    '320132': '08696',
    '319193': '025383',
    '32265': '012584',
    '31976': '04333',
    '30116': '025114',
    '319199': '011920',
    '319143': '022318',
    '32001': '015285',
    '31428': '014627',
    '31842': '016743',
    '30106': '016660',
    '31901': '018255',
}

# ____________________________________________________________________________________________________________________
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

men_articles_dict = {
    '10006': '014972',
    '11903': '026123',
    '12105': '024871',
    '12016': '025889',
    '12005': '023976',
    '12115': '018403',
    '11934': '025417',
    '10001': '02167',
    '10004': '027153',
    '11916': '026114',
    '11405': '025649',
    '10233': '024671',
    '11820': '025650',
    '11631': '020904',
    '11606': '021230',
    '11815': '013876',
    '11927': '013824',
    '10131': '023078',
    '11605': '047',
    '12024': '021084',
    '10022': '06997',
    '11401': '019021',
    '12208': '018397',
    '12109': '015652',
    '12010': '017012',
    '11514': '025363',
    '11724': '08875',
    '11624': '014948',
    '11725': '019832',
    '12009': '023332',
    '12210': '024190',
    '11512': '09886',
}


# ____________________________________________________________________________________________________________________
# Children
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

children_articles_dict = {
}

