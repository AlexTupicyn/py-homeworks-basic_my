from datetime import datetime

import bs4
import requests
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}

url = 'https://habr.com'
response = requests.get(url, headers=headers)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

KEYWORDS = ['design', 'photo', 'web', 'python']

articles = soup.find_all('article', class_='tm-articles-list__item')
for article in articles:
    hubs = article.find('h2', class_="tm-title")

    a_tag = hubs.find('a')
    relevate_link = a_tag['href']
    absolyut_link = f'{url}{relevate_link}'
    # print(absolyut_link)

    time_tag = article.find('time')
    data = time_tag['datetime']

    title = hubs.text
    # print(title)
    hub2 = title.lower().split()
    # print(hub2)

    # print(full_href)
    for hub in hub2:
        if hub in KEYWORDS:
            print(f'Название статьи: {title}\nДата выпуска: {data}\nСсылка на статью: {absolyut_link}', '\n')
