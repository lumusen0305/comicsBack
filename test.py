import requests
from bs4 import BeautifulSoup
import urllib
import json
import time
from requests.api import get

from sqlalchemy.sql.expression import null
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
rep = {
"data": [],
"code": 200,
"msg": "null"
 }
link = 'https://www.manhuagui.com/comic/19430/'
r = requests.get(link, headers = headers)
soup = BeautifulSoup(r.text, 'lxml')
comic_table = soup.find_all('div',id='chapter-list-1')
chapter_list=comic_table[0].find_all('ul')
for chapter in chapter_list:
    chapter_detail=chapter.find_all('a',class_='status0')
    for item in reversed(chapter_detail):
        print(item.get('title'))
        print('https://www.manhuagui.com'+item['href'])