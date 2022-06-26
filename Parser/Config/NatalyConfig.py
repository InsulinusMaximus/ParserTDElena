import collections

# TDElena
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

halaty = ['https://natali37.ru/catalog/category/163?page=' + str(i) for i in range(1, 29+1)]
tuniky = ['https://natali37.ru/catalog/category/164?page=' + str(i) for i in range(1, 43+1)]
sarafan = ['https://natali37.ru/catalog/category/165?page=' + str(i) for i in range(1, 8+1)]
platya = ['https://natali37.ru/catalog/category/166?page=' + str(i) for i in range(1, 33+1)]
kostyumy = ['https://natali37.ru/catalog/category/167?page=' + str(i) for i in range(1, 62+1)]
sorochki = ['https://natali37.ru/catalog/category/171?page=' + str(i) for i in range(1, 23+1)]
penyuary = ['https://natali37.ru/catalog/category/172?page=' + str(i) for i in range(1, 4+1)]
pizhamy = ['https://natali37.ru/catalog/category/173?page=' + str(i) for i in range(1, 15+1)]
futbolky = ['https://natali37.ru/catalog/category/174?page=' + str(i) for i in range(1, 24+1)]
tolstovki = ['https://natali37.ru/catalog/category/177?page=' + str(i) for i in range(1, 13+1)]
zhakety = ['https://natali37.ru/catalog/category/178?page=' + str(i) for i in range(1, 3+1)]
kurtki = ['https://natali37.ru/catalog/category/179?page=']
bryuki = ['https://natali37.ru/catalog/category/180?page=' + str(i) for i in range(1, 11+1)]
bridzhi = ['https://natali37.ru/catalog/category/181?page=' + str(i) for i in range(1, 3+1)]
shorty = ['https://natali37.ru/catalog/category/182?page=' + str(i) for i in range(1, 3+1)]
yubki = ['https://natali37.ru/catalog/category/183?page=' + str(i) for i in range(1, 4+1)]
sportivnaya_odezhda = ['https://natali37.ru/catalog/category/731?page=' + str(i) for i in range(1, 23+1)]

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

category = 'Women'
articles = collections.namedtuple(
    category,
    (
        'TD_Elena',
        'Nataly'
    )
)

articles_nataly = (
    '025188',
    '011200',
    '08130',
    '055016',
    '025575',
    '015567',
    '032042',
    '08080',
    '026683',
    '027724',
    '025761',
    '024726',
    '03677',
    '012425',
    '021101',
    '015032',
    '025196',
    '024328',
    '017905',
    '024807',
    '012801',
    '024035',
    '025130',
    '025254',
    '020476',
    '025808',
    '05387',
    '01583',
    '08508',
    '024187',
    '026195',
    '025682',
    '04931',
    '025703',
    '023053',
    '018203',
    '024360',
    '09234',
    '05534',
    '021844',
    '020550',
    '08696',
    '025383',
    '012584',
    '04333',
    '025114',
    '011920',
    '022318',
    '015285',
    '027561',
    '014627',
    '016743',
    '016660',
    '018255',
)

articles_td_elena = (
    '32291',
    '31822',
    '31946',
    '31430',
    '322107',
    '31969',
    '322165',
    '322125',
    '321165',
    '31729',
    '32139',
    '320165',
    '30040',
    '315159',
    '31757',
    '31758',
    '32247',
    '32189',
    '32049',
    '32221',
    '32242',
    '32070',
    '32229',
    '320129',
    '320103',
    '322105',
    '32058',
    '32251',
    '32275',
    '32276',
    '32227',
    '32268',
    '32011',
    '32111',
    '321153',
    '32263',
    '322102',
    '31587',
    '320184',
    '31497',
    '319216',
    '320132',
    '319193',
    '32265',
    '31976',
    '30116',
    '319199',
    '319143',
    '32001',
    '31428х',
    '31842',
    '30106',
    '31901',
)

women_articles = articles(
    Nataly=articles_nataly,
    TD_Elena=articles_td_elena
)

# ____________________________________________________________________________________________________________________
# Men
product_category_name = 'Women'
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

kostyumy = ['https://natali37.ru/catalog/category/210?page=' + str(i) for i in range(1, 6+1)]
futbolky = ['https://natali37.ru/catalog/category/213?page=' + str(i) for i in range(1, 21+1)]
tolstovki = ['https://natali37.ru/catalog/category/215?page=' + str(i) for i in range(1, 7+1)]
bryuki = ['https://natali37.ru/catalog/category/217?page=' + str(i) for i in range(1, 5+1)]
halaty = ['https://natali37.ru/catalog/category/220?page=1']
shorty = ['https://natali37.ru/catalog/category/219?page=' + str(i) for i in range(1, 4+1)]
pizhamy = ['https://natali37.ru/catalog/category/314?page=']
kurtki = ['https://natali37.ru/catalog/category/581?page=']

men_urls = category_url(
    kostyumy,
    futbolky,
    tolstovki,
    bryuki,
    halaty,
    shorty,
    pizhamy,
    kurtki,
    )

men_articles = (
    '014972',
    '026123',
    '024871',
    '025889',
    '023976',
    '018403',
    '025417',
    '002167',
    '027153',
    '026114',
    '025649',
    '024671',
    '025650',
    '020904',
    '021230',
    '013876',
    '013824',
    '023078',
    '000047',
    '021084',
    '006997',
    '019021',
    '018397',
    '015652',
    '017012',
    '025363',
    '008875',
    '014948',
    '019832',
    '023332',
    '024190',
    '009886',
)



