import uuid
import requests
from bs4 import BeautifulSoup
from sqlalchemy import text
from sqlalchemy.sql.expression import null
from . import comic
from flask import request, jsonify
from flask import Response
import json
import re
from urllib.parse import urlparse

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}

@comic.route('/getComic' , methods=['POST'])
def getComic():
    params=request.json
    page=int(params["page"])
    rep = {
    "data": [],
    "code": 200,
    "msg": "null"
     }
    link = 'https://www.baozimh.com/classify?page='+str(page)
    r = requests.get(link, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')
    comic_table = soup.find_all('div',class_='comics-card pure-u-1-3 pure-u-md-1-4 pure-u-lg-1-6')
    for comic in comic_table:
        comic_img=comic.find_all('amp-img')
        comic_title=comic.find_all('a',class_='comics-card__info')
        rep["data"].append({'name':comic_img[0].get('alt'),'url':'https://www.baozimh.com'+comic_title[0].get('href'),'image':comic_img[0].get('src'),'author':comic_title[0].find_all('small')[0].text.replace('\n', '').replace(' ', '')})
    return Response(json.dumps(rep),  mimetype='application/json')

@comic.route('/getComicList' , methods=['POST'])
def getComicList():
    params=request.json
    comic_url=params["comic_url"]
    rep = {
    "data": [],
    "code": 200,
    "msg": "null"
     }
    r = requests.get(comic_url, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')
    chapter = soup.find('div',id='chapter-items')
    chapterlist=chapter.find_all('a',class_='comics-chapters__item')
    for comic in chapterlist:
        parsed_result=urlparse(comic.get('href'))
        res=re.split('&|=',parsed_result.query)
        url='https://www.webmota.com/comic/chapter/'+res[1]+'/'+res[3]+'_'+res[5]+'.html'
        chapter_image = requests.get(url, headers = headers)
        chapter_image_soup = BeautifulSoup(chapter_image.text, 'lxml')
        chapter_image_img = chapter_image_soup.find('img',class_='comic-contain__item')
        rep["data"].append({'chapter':comic.find('span').text,'url':url,'image':chapter_image_img.get('data-src')})
    return Response(json.dumps(rep),  mimetype='application/json')


@comic.route('/getComicMoreList' , methods=['POST'])
def getComicMoreList():
    params=request.json
    comic_url=params["comic_url"]
    rep = {
    "data": [],
    "code": 200,
    "msg": "null"
     }
    r = requests.get(comic_url, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')
    chapter = soup.find('div',id='chapters_other_list')
    chapterlist=chapter.find_all('a',class_='comics-chapters__item')
    for comic in chapterlist:
        parsed_result=urlparse(comic.get('href'))
        res=re.split('&|=',parsed_result.query)
        url='https://www.webmota.com/comic/chapter/'+res[1]+'/'+res[3]+'_'+res[5]+'.html'
        rep["data"].append({'chapter':comic.find('span').text,'url':url,'image':'https://static-tw.baozimh.com/cover/gongjiaonannubaoxiaomanhua-wuyiboruntong.jpg'})
    return Response(json.dumps(rep),  mimetype='application/json')

@comic.route('/getComicDetail' , methods=['POST'])
def getComicDetail():
    params=request.json
    comic_url=params["comic_url"]
    rep = {
    "data": [],
    "code": 200,
    "msg": "null"
     }
    r = requests.get(comic_url, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')
    chapter = soup.find('p')
    rep["data"].append({'detail':chapter.text})
    return Response(json.dumps(rep),  mimetype='application/json')
@comic.route('/getReadPage' , methods=['POST'])
def getReadPage():
    params=request.json
    read_page=params["read_page"]
    rep = {
    "data": [],
    "code": 200,
    "msg": "null"
     }
    r = requests.get(read_page, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')
    comic_img = soup.find_all('img',class_='comic-contain__item')
    for item in comic_img:
        rep["data"].append({'image':item.get('data-src')})
    return Response(json.dumps(rep),  mimetype='application/json')
