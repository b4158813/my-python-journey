import re
import os
import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
from config1 import *
import pymongo
from hashlib import md5
from multiprocessing import Pool
from json.decoder import JSONDecodeError


client=pymongo.MongoClient(MONGO_URL,connect=False)
db = client[MONGO_DB]

def get_page_index(offset, keyword):  # 请求索引页
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'en_qc': 1,
        'cur_tab': 1
    }
    # 得到最原始的url，再加上data
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)  # 把字典对象转化成url的请求参数
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text  # 得到索引页面源代码
        return None
    except RequestException:
        print('请求索引页出错')
        return None


def parse_page_index(html):  # 解析索引页
    try:
        data = json.loads(html)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except JSONDecodeError and TypeError:
        pass

def get_page_detail(url):  # 请求详情页
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求详情页出错')
        return None


def parse_page_detail(html,url):#解析详情页
    try:
        title = re.search('.*?articleInfo.*?title:\s\'(.*?)\'.*?',re.S)
        images_pattern = re.compile('gallery:\sJSON.parse\("(.*?)"\),', re.S)
        result = re.search(images_pattern, html)
        if result:
            data = json.loads(result.group(1))
            if data and 'sub_images' in data.keys():
                sub_images = data.get('sub_images')
                images = [item.get('url') for item in sub_images]
                for image in images: download_image(image)
                return {
                    'title':title,
                    'url':url,
                    'image':images
                }
    except IndexError:
        pass

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到MONGODB成功',result)
        return True
    return False

def download_image(url):
    print('正在下载',url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求图片出错')
        return None

def save_image(content):
    file_path='{0}/{1}.{2}'.format(os.getcwd(),md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()


def main(offset):
    html = get_page_index(offset,KEYWORD)
    for url in parse_page_index(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html,url)
            if result: save_to_mongo(result)

if __name__ == '__main__':
    groups = [x*20 for x in range(GROUP_START,GROUP_END+1)]
    pool = Pool()
    pool.map(main,groups)
