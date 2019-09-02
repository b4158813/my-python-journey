import re
from selenium import webdriver
import requests
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get('http://bang.dangdang.com/books/fivestars/1-1')

js="var action=document.documentElement.scrollTop=10000"
browser.execute_script(js)
time.sleep(3)

html = browser.page_source#特别注意这里获取的是不完整的

# 用requests获取的源代码是完整的
html2=requests.get('http://bang.dangdang.com/books/fivestars/1-1').text

print(html==html2)
with open('html_html2.txt','w',encoding='utf-8') as f:
    f.write(html+10*'\n'+html2)
# pattern = re.compile(
#     '<li>.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><span\sclass="price_n">&yen;(.*?)</span>.*?</li>',
#     re.S)
#
# items = re.findall(pattern, html)
# print(items)
