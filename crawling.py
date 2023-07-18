import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from home.models import Velog

def crawl_velog():
    req = requests.get('https://velog.io/')
    html = req.content.decode('utf-8', 'replace')
    soup = BeautifulSoup(html, 'html.parser')
    velog_elements = soup.select('main > div > div')
    
    velog_list = []

    for velog_element in velog_elements:
        title = velog_element.select_one('div > a > h4').text.strip()
        author = velog_element.select_one('div > a > span > b').text.strip()
        date = velog_element.select_one('div > div > span').text.strip()
        url = velog_element.select_one('div > a')['href']

        velog = {
            "title": title,
            "author" : author,
            "date": date,
            "url" : url,
        }
        print("Title:", velog["title"])
        print("Author:", velog["author"])
        print("Date:", velog["date"])
        print("URL :", velog["url"])
        print("-----")
        velog_list.append(velog)

    return velog_list

if __name__ == '__main__':
    velog_list = crawl_velog()  # 제목 리스트를 미리 가져옴
    for velog_data in velog_list: #db 저장
        a = Velog(title = velog_data["title"], 
                  author = velog_data["author"], 
                  date = velog_data["author"],
                  url = velog_data["url"])
        a.save()