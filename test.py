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
link = 'https://www.webmota.com/comic/chapter/wuni-iciyuandongman/0_159.html'
r = requests.get(link, headers = headers)
soup = BeautifulSoup(r.text, 'lxml')
chapter = soup.find('img',class_='comic-contain__item')
print(chapter.get('data-src'))
