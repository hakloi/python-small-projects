import requests
import csv
from bs4 import BeautifulSoup


def get_request_structure():
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 YaBrowser/26.4.0.0 Safari/537.36"
    ACCEPT = "text/html"

    headers = {
        "Accept": ACCEPT,
        "User-Agent": USER_AGENT
    }

    req = requests.get("https://cbr.ru/currency_base/daily/", headers)
    src = req.text

    soup = BeautifulSoup(src, 'lxml')
    return soup


def get_currencies(soup):
    currencies = soup.find_all("tr")

    with open("web-scrapper/currencies.csv", "w", newline = '', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=',')

        for currency in currencies:
            attributes = list(currency.text.strip().split("\n"))
            writer.writerows([attributes])
        print("Data saved!")
        
        
def get_date_currencies(soup):
    date = soup.find("button", class_="datepicker-filter_button").text
    return date

# example
soup = get_request_structure()
get_currencies(soup)
get_date_currencies(soup)