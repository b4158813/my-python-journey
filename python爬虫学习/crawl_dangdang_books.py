import requests
import re
import time
import json


def main(page):
    url = 'http://bang.dangdang.com/books/fivestars/1-' + str(page)  # 获取不同页数的url
    html = request_dandan(url)  # 针对该页面发送请求，获取内容
    items = parse_result(html)  # 针对内容 解析过滤我们想要的信息（是一个生成器）
    # 将解析好的每页内容（生成器）写入文件
    for item in items:
        write_item_to_file(item)


# 请求当当网的方法
def request_dandan(url):
    try:
        response = requests.get(url)  # 发送get请求
        if response.status_code == 200:  # 如果正常响应
            return response.text  # 返回内容
    except requests.RequestException:  # 出错则返回none
        return None


# 解析当当网的方法
def parse_result(html):
    # 正则表达式将需要过滤的信息格式打包
    pattern = re.compile(
        '<li>.*?<div.*?list_num.*?(\d+).</div>.*?<img src="(.*?)".*?title="(.*?)"/></a></div>.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span>.*?class="price_n">&yen;(.*?)</span>.*?</li>',
        re.S)
    # 找到所有符合的信息（返回一个list）
    items = re.findall(pattern, html)
    # 创建生成器生成一个dict，以便写入文件
    for item in items:
        yield {
            'range': item[0],
            'image': item[1],
            'title': item[2],
            'recommend': item[3],
            'author': item[4],
            'times': item[5],
            'price': item[6]
        }


# 将解析好的信息写入文件的方法
def write_item_to_file(item):
    print("开始写入数据 ====> " + str(item))
    with open('dangdang_book.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')  # 写入每本书的数据并换行
        f.close()


if __name__ == '__main__':
    i = 1
    while i < 26:  # 该榜单一共有25页，一页一页获取并写入文件
        main(i)
        i += 1
