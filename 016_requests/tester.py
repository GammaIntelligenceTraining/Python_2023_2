import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError

# 200 - 299 Success
# 300 - 399 Redirect
# 400 - 499 Client error
# 500 - 599 Server error
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
#                          ' (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
#
# r = requests.get('https://xkcd.com/353/')
#
# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.a['href'])
# match = soup.find('div', id='middleContainer')
# print(match.div.text)

# matches = soup.find_all('div', class_='box')
# print(len(matches))
# print(matches)
# for match in matches:
#     print(match.get_attribute_list('class'))
# md_container = soup.find('div', id='middleContainer')
# matches = md_container.find_all('a')
# for match in matches:
#     if 'https://' not in match['href']:
#         print('https://xkcd.com', match['href'], sep='')
#     else:
#         print(match['href'])

# match = soup.find_all('div', string='Python')
import re
# match = soup.find_all('a', href=True, limit=2)
# for match in match:
#     print(match)

# first_link = soup.find('a', href='https://xkcd.com/353')
# print(first_link.chi)
# first_div = soup.find('div')
# print(list(first_div.strings))


import datetime
url = 'https://dashboard.elering.ee/api/nps/price?start=2024-02-12T20%3A59%3A59.999Z&end=2024-02-14T20%3A59%3A59.999Z'
response = requests.get(url)
json_data = response.json()
for day in json_data['data']['ee']:
    dt = datetime.datetime.fromtimestamp(day['timestamp'])
    price = day['price']
    print(dt, price)