import re
import requests
import json
from requests.exceptions import RequestException


def get_one_page(url):
    try:
        response=requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern=re.compile('<dd>.*?movie-item".*?data-src="(.*?)@160w.*?movie-item-title"\stitle="(.*?)">',re.S)
    items=re.findall(pattern,html)
    for item in items:
        # print(item)
        yield {
            'image':item[0],
            'title':item[1],
        }

def write_to_file(content):
    with open('crawl_maoyan_suspense_movie.txt','a',encoding='utf-8') as f:
        print('开始写入文件 ==>')
        print(content)
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main(page):
    url='https://maoyan.com/films?showType=3&catId=8&sortId=3&offset='+str(page)
    html=get_one_page(url)
    # print(html)
    items=parse_one_page(html)
    for item in items:
        write_to_file(item)

if __name__ == '__main__':
    for i in range(6):
        main(i*30)