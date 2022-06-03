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

halaty = ['https://natali37.ru/catalog/category/163?page=' + str(i) for i in range(1, 26)]
tuniky = ['https://natali37.ru/catalog/category/164?page=' + str(i) for i in range(1, 43)]
sarafan = ['https://natali37.ru/catalog/category/165?page=' + str(i) for i in range(1, 8)]
platya = ['https://natali37.ru/catalog/category/166?page=' + str(i) for i in range(1, 33)]
kostyumy = ['https://natali37.ru/catalog/category/167?page=' + str(i) for i in range(1, 62)]
sorochki = ['https://natali37.ru/catalog/category/171?page=' + str(i) for i in range(1, 23)]
penyuary = ['https://natali37.ru/catalog/category/172?page=' + str(i) for i in range(1, 4)]
pizhamy = ['https://natali37.ru/catalog/category/173?page=' + str(i) for i in range(1, 15)]
futbolky = ['https://natali37.ru/catalog/category/174?page=' + str(i) for i in range(1, 24)]
tolstovki = ['https://natali37.ru/catalog/category/177?page=' + str(i) for i in range(1, 13)]
zhakety = ['https://natali37.ru/catalog/category/178?page=' + str(i) for i in range(1, 3)]
kurtki = ['https://natali37.ru/catalog/category/179?page=']
bryuki = ['https://natali37.ru/catalog/category/180?page=' + str(i) for i in range(1, 11)]
bridzhi = ['https://natali37.ru/catalog/category/181?page=' + str(i) for i in range(1, 3)]
shorty = ['https://natali37.ru/catalog/category/182?page=' + str(i) for i in range(1, 3)]
yubki = ['https://natali37.ru/catalog/category/183?page=' + str(i) for i in range(1, 4)]
sportivnaya_odezhda = ['https://natali37.ru/catalog/category/731?page=' + str(i) for i in range(1, 23)]

nataly_urls = []
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

# Men
product_category_name = 'Men'
categories = collections.namedtuple(
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

halaty = ['https://natali37.ru/catalog/category/163?page=' + str(i) for i in range(1, 26)]
tuniky = ['https://natali37.ru/catalog/category/164?page=' + str(i) for i in range(1, 43)]
sarafan = ['https://natali37.ru/catalog/category/165?page=' + str(i) for i in range(1, 8)]
platya = ['https://natali37.ru/catalog/category/166?page=' + str(i) for i in range(1, 33)]
kostyumy = ['https://natali37.ru/catalog/category/167?page=' + str(i) for i in range(1, 62)]
sorochki = ['https://natali37.ru/catalog/category/171?page=' + str(i) for i in range(1, 23)]
penyuary = ['https://natali37.ru/catalog/category/172?page=' + str(i) for i in range(1, 4)]
pizhamy = ['https://natali37.ru/catalog/category/173?page=' + str(i) for i in range(1, 15)]
futbolky = ['https://natali37.ru/catalog/category/174?page=' + str(i) for i in range(1, 24)]
tolstovki = ['https://natali37.ru/catalog/category/177?page=' + str(i) for i in range(1, 13)]
zhakety = ['https://natali37.ru/catalog/category/178?page=' + str(i) for i in range(1, 3)]
kurtki = ['https://natali37.ru/catalog/category/179?page=']
bryuki = ['https://natali37.ru/catalog/category/180?page=' + str(i) for i in range(1, 11)]
bridzhi = ['https://natali37.ru/catalog/category/181?page=' + str(i) for i in range(1, 3)]
shorty = ['https://natali37.ru/catalog/category/182?page=' + str(i) for i in range(1, 3)]
yubki = ['https://natali37.ru/catalog/category/183?page=' + str(i) for i in range(1, 4)]
sportivnaya_odezhda = ['https://natali37.ru/catalog/category/731?page=' + str(i) for i in range(1, 23)]

nataly_urls = []
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




