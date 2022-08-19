import requests
from Parser.Config import TDValeriayConfig

print(type(TDValeriayConfig.men_urls))

for pages in TDValeriayConfig.men_urls:
    for page in pages:
        req = requests.get(page)

        print(req.text)

