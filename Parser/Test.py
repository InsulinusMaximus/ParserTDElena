import requests
import lxml
import bs4

url = 'https://td-elena.ru/catalog/muzhskaya_odezhda/bryuki_1/'
req = requests.get(url)


path = 'C:/Users/Pavel/PycharmProjects/TDElenaParser/test_TDElena.txt'
with open(path, 'w', encoding="utf-8", newline="") as f:
    f.write(req.text)

soup = bs4.BeautifulSoup(req.text, 'html.parser')
path = 'C:/Users/Pavel/PycharmProjects/TDElenaParser/test_TDElenaSoup.txt'
with open(path, 'w', encoding="utf-8", newline="") as f:
    f.write(soup.text)

print(soup)