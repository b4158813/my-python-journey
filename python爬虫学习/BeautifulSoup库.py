'''
大总结：
    -推荐使用lxml解析，必要时使用html.parser
    -标签选择筛选功能弱但是速度快
    -建议使用find()、find_all()查询匹配单个结果或多个结果
    -如果对CSS选择器熟悉建议使用select()
    -记住常用的获取属性和文本值得方法
'''

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup  # 导入模块

soup = BeautifulSoup(html, 'lxml')  # 以lxml解析库解析html代码
# print(soup.prettify())  # 自动格式化代码，补全格式
# print(soup.title.string)  # 输出title的字符串

# 标签内容
print(soup.title)  # 打印出包括title标签的内容
print(type(soup.title))  # Tag类型
print(soup.head)  # 打印出包括head标签的内容
print(soup.p)  # 只会返回选择的第一个p标签内容

print(10 * '-')
# 获取名称
print(soup.title.name)  # 打印出外层标签名称

print(10 * '-')
# 获取属性
print(soup.p.attrs['name'])  # 获取第一个p标签name属性的值
print(soup.p['name'])  # 同上

print(10 * '-')
# 获取内容
print(soup.p.string)  # 获取第一个p标签的内容

print(10 * '-')
# 嵌套选择
print(soup.head.title.string)  # 获取head标签内的title标签内的内容

print(20 * '-')
html1 = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""
# 子节点和子孙节点
# contents方法获取子节点（返回一个list）
# children方法获取子节点（返回一个Iterator）
# descendants方法获取子孙节点（返回一个Iterator）
soup = BeautifulSoup(html1, 'lxml')
print(soup.p.contents)  # 获取p的所有子节点（返回一个list）

print(10 * '-')
print(soup.p.children)  # children方法生成一个子节点的Iterator
for i, child in enumerate(soup.p.children):  # 需要用for循环打印
    print(i, child)  # 获取所有的子节点

print(10 * '-')
print(soup.p.descendants)  # descendants方法生成一个子孙节点的Iterator
for i, child in enumerate(soup.p.descendants):
    print(i, child)  # 获取所有的子孙节点

print(10 * '-')
# 父节点和祖先节点
print(soup.a.parent)  # 获取父节点（这里是p标签）内容
print(10 * '-')
print(list(enumerate(soup.a.parents)))  # 获取所有祖先节点（迭代器）

print(10 * '-')
# 兄弟节点
print(list(enumerate(soup.a.next_siblings)))  # 获取之后的兄弟节点
print(list(enumerate(soup.a.previous_siblings)))  # 获取前面的兄弟节点

print(20 * '-')
html2 = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
# 标准选择器 find_all(name,attrs,recursive,text,**kwargs)
# 根据标签、属性、内容查找文档
# 根据标签查找
soup = BeautifulSoup(html2, 'lxml')
print(soup.find_all('ul'))  # 输出所有'ul'标签（返回一个list）
print(type(soup.find_all('ul')[0]))
print(10 * '-')
for ul in soup.find_all('ul'):  # 嵌套打印ul标签内的li标签
    print(ul.find_all('li'))

# attrs通过属性名查找
print(10 * '-')
print(soup.find_all(attrs={'id': 'list-1'}))  # 通过id属性名查找
print(10 * '-')
print(soup.find_all(id='list-1'))  # 同上，更加方便
print(10 * '-')
print(soup.find_all(class_='element'))  # 通过class查找

# text通过文本内容查找
print(10 * '-')
print(soup.find_all(text='Foo'))  # 返回的是内容

# find(name,attrs,recursive,text,**kwargs)
# find返回单个元素，find_all返回所有元素
print(10 * '-')
print(soup.find('ul'))  # 返回满足条件的第一个元素（这里是第一个ul标签）
print(type(soup.find('ul')))  # Tag类型
print(soup.find('page'))  # 未发现满足内容沢返回None

'''
除此之外，还有find_parents() find_all_next() 等查找方法
'''

print(20 * '-')
# CSS选择器
# 通过select()直接传入CSS选择器即可完成选择
# . -> class
# # -> id
# 标签不用加 < >
# 如果查找的是class则直接在名称前加“.”表示为class即可
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))  # 返回所有ul标签下的li标签内容
print(soup.select('#list-2 .element'))  # 返回所有id为list-2标签下的class为element标签的内容
print(type(soup.select('ul')[0]))  # Tag类型，可迭代查找并输出

print(10 * '-')
for ul in soup.select('ul'):  # 嵌套获取每个ul标签下的li标签
    print(ul.select('li'))
print(10 * '-')
#获取ul标签下的id内容
for ul in soup.select('ul'):
    print(ul['id'])#获取id属性内容
    print(ul.attrs['id'])#同上
print(10 * '-')
#获取所有li标签下的内容
for li in soup.select('li'):
    print(li.get_text())


