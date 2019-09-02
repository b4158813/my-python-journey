html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq

# 字符串初始化
doc = pq(html)
print(doc('li.item-1'))  # 传入css选择器
print(10 * '-')

# 字符串初始化
doc = pq(url='http://www.baidu.com')  # 传入url
print(doc('head'))  # 返回head标签内容

# #文件初始化
# doc=pq(filename='demo.html')
# print(doc('li'))

html1 = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
print(10 * '-')
# 基本CSS选择器
doc = pq(html1)
print(doc('#container .list li'))  # 空格代表一层嵌套关系

print(10 * '-')
# 查找元素
items = doc('.list')
print(type(items))  # 类型为pyquery对象（可以嵌套查找）
print(items)

print(10 * '-')
lis = items.find('li')  # 查找子元素（较方便）
print(type(lis))
print(lis)

print(10 * '-')
lis2 = items.children('.active')  # 查找直接子元素
print(lis2)  # 这里打印结果同上

print(10 * '-')
# 查找父元素
doc = pq(html1)
items = doc('.list')
container = items.parent()  # 返回父元素
print(type(container))  # 类型为pyquery对象
print(container)

html3 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
print(20 * '-')
# 查找祖先元素
doc = pq(html3)
items = doc('.list')
parents = items.parents()  # 返回祖先元素 和 直接父元素
print(type(parents))  # pyquery对象
print(parents)

print(10 * '-')
# 获取兄弟元素
li = doc('.list .item-0.active')  # 空格代表下一层，无空格代表并列层
print(li.siblings())  # 返回除了li之外的其他标签
print(10 * '-')
print(li.siblings('.active'))  # 嵌套筛选出class含有active的标签

print(10 * '-')
# 遍历
doc = pq(html3)
lis = doc('li').items()
print(type(lis))  # 生成器类型
for li in lis:
    print(li)

print(10 * '-')
# 获取属性、文本
a = doc('.item-0.active a')
print(a)
print(a.attr('href'))  # 获取a属性值
print(a.attr.href)  # 同上
print(a.text())  # 获取文本

print(10 * '-')
# 获取HTML
li = doc('.item-0.active')
print(li)
print(li.html())  # 获取li里面的所有html

print(20 * '-')
html4 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
# DOM操作
# addClass&removeClass
doc = pq(html4)
li = doc('.item-0.active')
print(li)
li.removeClass('active')  # 移除class属性的active
print(li)
li.addClass('active')  # 添加class属性的active
print(li)

print(10 * '-')
# attr&css
li = doc('.item-0.active')
li.attr('name', 'link')  # 添加name属性
print(li)
li.css('font-size', '14px')  # 添加style属性
print(li)

print(10 * '-')
html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''
# remove操作（较常用）
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()  # 移除p标签内容
print(wrap.text())




html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
#伪类选择器
print(20*'-')
doc = pq(html)
li = doc('li:first-child')#获取第一个li标签
print(li)
li = doc('li:last-child')#获取最后一个li标签
print(li)
li = doc('li:nth-child(2)')#获取第二个li标签
print(li)
li = doc('li:gt(2)')#获取第2（这里0是第一个）个以后的li标签
print(li)
li = doc('li:nth-child(2n)')#获取偶数序号的标签（2、4、6、8）
print(li)
li = doc('li:contains(second)')#获取包含second文本的标签
print(li)