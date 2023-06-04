from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = "https://rezka.ag/films/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"
}

def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response




def get_data_from_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all(
        'div', class_="b-content__inline_item"
    )
    films = []
    for item in items:
        info = item.find('div', class_="b-content__inline_item-link").find('div').getText().split(", ")
        film = {
            "title": item.find('div', class_="b-content__inline_item-link").find('a').getText(),
            #.string, можно импользовать место getText()
            "link": item.find('div', class_="b-content__inline_item-link").find('a').get("href"),
            "year": info[0],
            "country": info[1],
            "genre": info[2]
        }
        films.append(film)

    return films

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        films = []
        for i in range(1, 2):
            html = get_html(f"{URL}page/{i}/")
            current_page = get_data_from_page(html.text)
            films.extend(current_page)
        return films
    else:
        raise Exception("Error in parser")

# pprint(parser())
# html = get_html(URL)
# get_data_from_page(html.text)
# print(html.text)
