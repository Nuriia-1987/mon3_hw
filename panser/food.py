import requests
from bs4 import BeautifulSoup

URL = "https://dostavka312.kg/garnirygpt/dodo-pizza"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_date(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_='spacer')
    # print(items)
    food = []
    for item in items:
        food.append({
            'title': item.find('p', class_='product-name').getText(),
            'disc': item.find('p', class_='product-descript').getText(),
            'price': item.find('div', class_='product-price').getText(),
            'photo': item.find('img').get('src')
        })
    # print(food)
    return food


# html1 = get_html(URL)
# get_date(html1.text)


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = []
        for i in range(0, 1):
            # html = get_html(f"{URL} i {i}.php")
            answer.extend(get_date(html.text))
        return answer
    else:
        raise Exception("Error in parser!")
