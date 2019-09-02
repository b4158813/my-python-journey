import re

# .*?匹配任意的字符，除了\n \r
content1 = 'wuluoxiang has 100 apples'
content2 = '''wuluoxiang has
 200 apples
'''
content3 = '''wuluoxiang has 100 apples
wuluoxiang has 200 apples
wuluoxiang has 300 apples
wuluoxiang has 400 apples'''
res1 = re.match('^w.*?(\d+)\s.*s$', content1)  # 注意此处要用贪心量化
# 如果有换行，则要更换re匹配模式为re.S
res2 = re.match('^w.*?(\d+)\s.*s$', content2, re.S)
# search方法自动匹配字符串，并返回第一个结果
res2_1 = re.search('w.*?(\d+)\s.*s', content2, re.S)
# 若内容很多，则使用findall方法获取所有匹配内容
res3 = re.findall('w.*?(\d+)\s.*?s', content3, re.S)  # 逐一这里两处非贪心量化

# sub方法 替换内容
res4 = re.sub('\d+', '250', content3)

# compile方法封装匹配符
pattern = re.compile('w.*?(\d+)\s.*?s', re.S)
res5 = re.match(pattern, content3)

print(res1.group(1))
print(res2.group(1))
print(res2_1.group(1))
print(res3)
print(res4)
print(res5.group(1))
