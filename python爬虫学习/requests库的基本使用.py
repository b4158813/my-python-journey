import requests

'''
# 一行代码get
r1 = requests.get('https://api.github.com/events')
# 一行代码post
r2 = requests.post('https://httpbin.org/post', data={'key': 'value'})
# 其他乱七八糟的HTTP请求
r3 = requests.put('https://httpbin.org/put', data={'key': 'value'})
r4 = requests.delete('https://httpbin.org/delete')
r5 = requests.head('https://httpbin.org/get')
r6 = requests.options('https://httpbin.org/get')

# 携带请求参数
payload={'key1':'value1','key2':'value2'}
r7=requests.get('https://httpbin.org/get',params=payload)

#假装自己是浏览器
url='https://api.github.com/some/endpoint'
headers={'user-agent':'my-app/0.0.1'}
r8=requests.get(url,headers=headers)
'''


'''
# 获取服务器响应文本内容
r9 = requests.get('https://api.github.com/events', stream=True)
print(r9.text)
print(r9.encoding)
# 获取响应字节内容
print(r9.content)
# 获取响应码
print(r9.status_code)
# 获取响应头
print(r9.headers)
# 获取json响应内容
print(r9.json())
# 获取socket流响应内容
print(r9.raw.read(10))
'''

'''
# POST请求 当你想要键里面添加多个值得时候
payload_dict = {'key1': ['value1', 'value2']}
r10 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r10.text)

#上传文件
url1='https://httpbin.org/post'
files={'file':open('h-s image.jpg','rb')}
r11=requests.post(url1,files=files)
print(r11.text)
'''

'''
#获取cookie信息
url2='http://example.com/some/cookie/setting/url'
r12=requests.get(url2)
# print(r12.cookies['example_cookie_name'])
'''

'''
#发送cookie信息
url3='https://httpbin.org/cookies'
cookies=dict(cookies_are='working')
r13=requests.get(url3,cookies=cookies)
print(r13.text)
'''
'''
#设置超时
requests.get('https://github.com/',timeout=0.001)
'''