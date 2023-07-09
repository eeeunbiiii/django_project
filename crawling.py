import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from home.models import Velog

def title_velog():
    req = requests.get('https://ko.wikipedia.org/wiki/%ED%8F%AC%ED%84%B8:%EC%9A%94%EC%A6%98_%ED%99%94%EC%A0%9C')
    html = req.content.decode('utf-8', 'replace')
    soup = BeautifulSoup(html, 'html.parser')
    velog_title = soup.select('#mw-content-text > div.mw-parser-output > table.vevent > tbody > tr > td > table > tbody > tr:nth-child(2) > td > ul > li:nth-child(1)')

    velog_list = []
    for title in velog_title:
        velog_list.append(title.text.strip())
        
    return velog_list

if __name__ == '__main__':
    title_list = title_velog()  # 제목 리스트를 미리 가져옴
    for title in title_list:
        a = Velog(title=title)
        a.save()