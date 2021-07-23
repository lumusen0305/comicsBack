import requests
from bs4 import BeautifulSoup
import urllib

import time
count = 0
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
link = 'https://www.manhuagui.com/list/view.html'
r = requests.get(link, headers = headers)
soup = BeautifulSoup(r.text, 'lxml')
comics = soup.find_all('ul',id="contList")
comics_list= comics[0].find_all('li')
# print(comics_list)
for item in comics_list:
    url = "https://www.manhuagui.com"+item.find('a')['href']
    name=item.find('a')['title']
    image=item.find_all('img')
    if image[0].get('data-src')!=None:
        src = image[0].get('data-src')
    else:
        src = image[0].get('src')
    star=item.find('em')