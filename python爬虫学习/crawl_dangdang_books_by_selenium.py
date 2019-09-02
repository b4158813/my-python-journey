import time
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

# 解析当当网的方法
def get_content():
    try:
        html = browser.page_source
        soup=BeautifulSoup(html,'lxml')#beautifulsoup解析html代码
        range=soup.select('.list_num')
        img=soup.select('.pic a img')
        title=soup.select('.name a')
        recommend=soup.select('.star .tuijian')
        author=soup.select('.publisher_info a')
        fivestar_amount=soup.select('.biaosheng span')
        price=soup.select('.price p .price_n')

        for i in range(20):
            yield {
                'range':range[i],
                'img':img[i]['src'],
                'title':title[i]['title'],
                'recomment':recommend[i],
                'author':author[i][title],
                'fivestar_amount':fivestar_amount[i],
                'price':price[i]
            }
        # 创建生成器生成一个dict，以便写入文件

    except TimeoutException:
        get_content()


def next_page(page):
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#t__cp')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#click_get_page')))
        input.clear()
        input.send_keys(page)
        submit.click()
    except TimeoutException:
        next_page(page)


# 将解析好的信息写入文件的方法
def write_item_to_file(item):
    print("开始写入数据 ====> " + str(item))
    with open('dangdang_book_by_selenium.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')  # 写入每本书的数据并换行
        f.close()


def main():
    url = 'http://bang.dangdang.com/books/fivestars/1-1'  # 获取第一页的url
    browser.get(url)  # 针对该页面发送请求，获取内容
    for i in range(2, 26):
        items = get_content()
        for item in items:
            write_item_to_file(item)
        next_page(i)


if __name__ == '__main__':
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)  # 等待响应
    main()
