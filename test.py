import requests
from bs4 import BeautifulSoup
import urllib
import json
import time
from requests.api import get
from urllib.parse import urlparse
import re
from sqlalchemy.sql.expression import null
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
rep = {
"data": [],
"code": 200,
"msg": "null"
 }
link = 'https://www.webmota.com/comic/chapter/jueshizhanhun-chuanqimanye/0_320.html'
r = requests.get(link, headers = headers)
soup = BeautifulSoup(r.text, 'lxml')
chapter_image_img = soup.find_all('img',class_='comic-contain__item')
for item in chapter_image_img:
    print(item.get('data-src'))