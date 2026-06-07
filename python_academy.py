import requests
from bs4 import BeautifulSoup

web = "https://python-academy.org/ru/trainer"

headers = {
        "Accept": "text/html",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 YaBrowser/26.4.0.0 Safari/537.36"
}

req = requests.get(web, headers)
src = req.content
soup = BeautifulSoup(src, 'lxml')

blocks = soup.select("div.sc-a9cca947-14.gTmWbm")
for block in blocks:
    link = block.find("a", class_="_blank")
    if link:
        print(link.get_text(strip=True))
