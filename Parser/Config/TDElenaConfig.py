import collections

# Nataly
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
        'bortsovki',
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

yubki = 'https://td-elena.ru/catalog/zhenskaya_odezhda/yubki_1/'
tuniky = ('https://td-elena.ru/catalog/zhenskaya_odezhda/tuniki/?PAGEN_1=' + str(i) for i in range(1, 2))
platya = ('https://td-elena.ru/catalog/zhenskaya_odezhda/plate/?PAGEN_1=' + str(i) for i in range(1, 7))
sarafan = ('https://td-elena.ru/catalog/zhenskaya_odezhda/sarafany/?PAGEN_1=' + str(i) for i in range(1, 2))
zhilety = 'https://td-elena.ru/catalog/zhenskaya_odezhda/zhilety/'
bluzony = ('https://td-elena.ru/catalog/zhenskaya_odezhda/bluzony/?PAGEN_1=' + str(i) for i in range(1, 2))
belye = 'https://td-elena.ru/catalog/zhenskaya_odezhda/bele_1/'
sportivnyye_kostyumy = (
    'https://td-elena.ru/catalog/zhenskaya_odezhda/kostyumy_sportivnye/?PAGEN_1=' + str(i) for i in range(1, 3)
    )
halaty = ('https://td-elena.ru/catalog/zhenskaya_odezhda/khalaty_1/?PAGEN_1=' + str(i) for i in range(1, 5))
kapri = 'https://td-elena.ru/catalog/zhenskaya_odezhda/kapri/'
futbolky = ('https://td-elena.ru/catalog/zhenskaya_odezhda/futbolki/?PAGEN_1=' + str(i) for i in range(1, 5))
topy = 'https://td-elena.ru/catalog/zhenskaya_odezhda/topy/?PAGEN_1='
bortsovki = 'https://td-elena.ru/catalog/zhenskaya_odezhda/bortsovki//?PAGEN_1='
vodolazki = 'https://td-elena.ru/catalog/zhenskaya_odezhda/vodolazki_1/?PAGEN_1='
mayki = 'https://td-elena.ru/catalog/zhenskaya_odezhda/mayki/?PAGEN_1='
dzhempery = ('https://td-elena.ru/catalog/zhenskaya_odezhda/dzhempery/?PAGEN_1=' + str(i) for i in range(1, 2))
rubashki = 'https://td-elena.ru/catalog/zhenskaya_odezhda/rubashki/?PAGEN_1='
tolstovki = ('https://td-elena.ru/catalog/zhenskaya_odezhda/tolstovki/?PAGEN_1=' + str(i) for i in range(1, 3))
sorochki = ('https://td-elena.ru/catalog/zhenskaya_odezhda/sorochki_1/?PAGEN_1=' + str(i) for i in range(1, 4))
pizhamy = ('https://td-elena.ru/catalog/zhenskaya_odezhda/pizhamy_komplekty_/?PAGEN_1=' + str(i) for i in range(1, 4))
shorty = ('https://td-elena.ru/catalog/zhenskaya_odezhda/shorty_1/?PAGEN_1=' + str(i) for i in range(1, 2))
bryuki = ('https://td-elena.ru/catalog/zhenskaya_odezhda/bryuki/?PAGEN_1=' + str(i) for i in range(1, 3))
bridzhi = 'https://td-elena.ru/catalog/zhenskaya_odezhda/bridzhi/?PAGEN_1='
losiny = 'https://td-elena.ru/catalog/zhenskaya_odezhda/losiny/?PAGEN_1='
velosipedki = 'https://td-elena.ru/catalog/zhenskaya_odezhda/velosipedki/?PAGEN_1='
kostyumy_domashniye = (
    'https://td-elena.ru/catalog/zhenskaya_odezhda/kostyumy_domashnie_1/?PAGEN_1=' + str(i) for i in range(1, 4)
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
    bortsovki=bortsovki,
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
'''
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

kostyumy = ['https://natali37.ru/catalog/category/210?page=' + str(i) for i in range(1, 6)]
futbolky = ['https://natali37.ru/catalog/category/213?page=' + str(i) for i in range(1, 21)]
tolstovki = ['https://natali37.ru/catalog/category/215?page=' + str(i) for i in range(1, 7)]
bryuki = ['https://natali37.ru/catalog/category/217?page=' + str(i) for i in range(1, 5)]
halaty = ['https://natali37.ru/catalog/category/220?page=1']
shorty = ['https://natali37.ru/catalog/category/219?page=' + str(i) for i in range(1, 4)]
pizhamy = ['https://natali37.ru/catalog/category/314?page=']
kurtki = ['https://natali37.ru/catalog/category/581?page=']

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
    
women_articles = (
    '10006',
    '11903',
    '12105П',
    '12016',
    '12005',
    '12115',
    '11934ВШ',
    '10001',
    '10004',
    '11916',
    '11405О',
    '10233',
    '11820',
    '11631',
    '11606',
    '11815',
    '11927Т',
    '10131',
    '11605',
    '12024',
    '10022',
    '11401А',
    '12208',
    '12109',
    '12010',
    '11514',
    '11724',
    '11624',
    '11725',
    '12009',
    '12210П',
    '11512',
)
'''