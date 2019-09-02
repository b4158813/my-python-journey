'''
urllib库的基本使用
'''

import socket
import urllib.error
import urllib.parse
# urlopen 发送get请求
import urllib.request

# response=urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

# 发送post请求
# data=bytes(urllib.parse.urlencode({'word':"hello"}),encoding='utf8')
# response=urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

# 发送get请求，超时返回错误
# try:
#    response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#    if isinstance(e.reason,socket.timeout):
#        print('TIME OUT')


response = urllib.request.urlopen('https://www.python.org')
print(type(response))
# 响应码、响应头
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))


