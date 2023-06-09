import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from home.models import Velog

def title_velog():
    req = requests.get('https://velog.io/@eunbi2222')
    html = req.content.decode('utf-8', 'replace')
    soup = BeautifulSoup(html, 'html.parser')
    velog_title = soup.select('#root > div.sc-efQSVx.sc-cTAqQK.hKuDqm > div.sc-Galmp.gifMhn.sc-jlRLRk.cluXqC > div:nth-child(4) > div.sc-uojGG.cQVKst > div > div:nth-child(1)')

    velog_list = []
    for title in velog_title:
        velog_list.append(title.text.strip())
        
    return velog_list

if __name__ == '__main__':
    title_list = title_velog()  # 제목 리스트를 미리 가져옴
    for title in title_list:
        a = Velog(title=title)
        a.save()