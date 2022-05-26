import csv

import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


payload = {'title_type': 'video_game', 'start': 1}
h = {'Accept-Language': 'en-US'}
url = "https://www.imdb.com/search/title/"

file = open('games.csv', 'w')
# file.write('Title,Rating,Year\n')

file_obj = csv.writer(file)
file_obj.writerow(['Title', 'Rating', 'Year'])

while payload['start'] < 400:
    r = requests.get(url, params=payload, headers=h)
    print(r.url)
    content = r.text

    soup = BeautifulSoup(content, "html.parser")

    block = soup.find("div", class_="lister-list")

    all_games = block.find_all('div', class_='lister-item')

    for each in all_games:
        title = each.h3.a.text
        year = each.find('span', class_='lister-item-year').text
        year = year.replace('(', '')
        year = year.replace(')', '')
        year = year.replace('I', '')

        rate = each.text
        print(rate)
        # file.write(title+' , '+rate+' , '+year+'\n')
        file_obj.writerow([title, rate, year])
    payload['start'] += 50
    sleep(randint(15, 20))
