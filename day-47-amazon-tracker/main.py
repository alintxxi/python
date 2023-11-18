import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/EKTOS-Charcoal-Washable-Emergency-Preparedness/dp/B0BJMZ19W2/ref=sr_1_1?crid=2EJ4L3NWLWP67&keywords=ektos&qid=1700334861&sprefix=ektos%2Caps%2C338&sr=8-1&th=1"
header = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Accept-Language": "en,fa;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)