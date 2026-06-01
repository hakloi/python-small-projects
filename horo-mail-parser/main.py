import requests
from bs4 import BeautifulSoup
import re
import json

website = "https://horo.mail.ru/prediction/CHOICE/today/?frommail=1"

def choice_sign(website):
    print()
    descr = """Choose your horoscope sign and write its number:
        Signs: 
        1. Aries
        2. Cancer
        3. Libra
        4. Capricorn
        5. Tauras
        6. Leo
        7. Pisces
        8. Gemini
        9. Virgo
        10. Sagittarius
        11. Aquarius
        12. Scorpio"""
    
    dct = {
        1: "aries", 
        2: "cancer", 
        3: "libra", 
        4: "capricorn", 
        5: "tauras", 
        6: "leo", 
        7: "pisces", 
        8: "gemini", 
        9: "virgo", 
        10: "sagittarius", 
        11: "aquarius",
        12: "scorpio"
        }
    
    while True:
        try:
            print(descr)
            
            user_choice = int(input("Input number: "))
            if 1 < user_choice > 12:
                print("Choose correct number from list!")
            break   
        except ValueError:
            print("Choose correct number from list!")
    
    webpage = website.replace("CHOICE", dct[user_choice])
    return webpage
       

def request_horo(webpage):
    headers = {
        "Accept": "text/html",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 YaBrowser/26.4.0.0 Safari/537.36"
    }
    
    req = requests.get(webpage, headers)
    src = req.content
    soup = BeautifulSoup(src, 'lxml')
    
    return soup


def parsing_info(soup):
    header = soup.find("title").text
    print(header, "\n")
    script = soup.find(attrs = {"id": "horo-script"})
    
    if script and script.string:
        html = script.string

        if 'window.__PRELOADED_STATE__ = ' in html:
            json_part = html.split('window.__PRELOADED_STATE__ = ')[1]
            json_str = json_part.rstrip(';')
            data = json.loads(json_str)

            text_blocks = data['page_data']['prediction']['text']
            
            full_html = ''.join(block['html'] for block in text_blocks)
            
            clean_html = re.sub(r'<[^>]+>', '', full_html)
            
            print(clean_html)
        else:
            print("Not found")

web = choice_sign(website)
soup = request_horo(web)
parsing_info(soup)
    