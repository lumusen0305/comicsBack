import uuid
import requests
from bs4 import BeautifulSoup
from sqlalchemy import text
from sqlalchemy.sql.expression import null
from . import comic
from flask import request, jsonify
from flask import Response
import json
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
    if page==1:
        link = 'https://www.manhuagui.com/list/view.html'
    else:
        link = 'https://www.manhuagui.com/list/view_p'+str(page)+'.html'
    r = requests.get(link, headers = headers)
    soup = BeautifulSoup(r.text, 'lxml')
    comics = soup.find_all('ul',id="contList")
    comics_list= comics[0].find_all('li')
    for item in comics_list:
        url = "https://www.manhuagui.com"+item.find('a')['href']
        name=item.find('a')['title']
        image=item.find_all('img')
        if image[0].get('data-src')!=None:
            src = image[0].get('data-src')
        else:
            src = image[0].get('src')
        star=item.find('em')
        star=int(float(star.text)/2)
        update_time=item.find_all('span')
        rep["data"].append({'name':name,'url':url,'image':src,'star':star,'update_time':update_time[3].text[:14]})
    return Response(json.dumps(rep),  mimetype='application/json')
