from urllib import request, parse
import ssl  # 用于处理https协议

# 使用ssl未经验证的上下文
context = ssl._create_unverified_context()
# 定义请求url和header
url = 'https://biihu.cc/account/ajax/login_process/'
headers = {
    # 假装自己是浏览器
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                  '/73.0.3683.103 Safari/537.36',
}
# 定义请求参数
dict = {
    'return_url': 'https://biihu.cc/',
    'user_name': 'b4158813',
    'password': '64158813',
    '_post_type': 'ajax',
}
# 把请求参数转化为byte
data = bytes(parse.urlencode(dict), 'utf-8')
# 封装request
req = request.Request(url, data=data, headers=headers, method='POST')
# 进行请求
response = request.urlopen(req, context=context)

print(response.read().decode('utf-8'))
