'''
Selenium
    自动化测试工具，支持多种浏览器
    爬虫主要用来解决JavaScript渲染的问题
'''
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser=webdriver.Chrome()
try:
    #用模拟浏览器发送get请求
    browser.get('https://www.baidu.com')
    #找到‘kw’元素
    input=browser.find_element_by_id('kw')
    #键入‘Python’内容
    input.send_keys('Python')
    #键入回车键
    input.send_keys(Keys.ENTER)
    #等待浏览器加载
    wait=WebDriverWait(browser,10)
    #等待ID为‘content_left’元素被加载出来
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    #打印出当前url
    print(browser.current_url)
    #打印当前cookies
    print(browser.get_cookies())
    #打印网页源代码
    print(browser.page_source)
finally:#成功就关闭浏览器
    browser.close()
'''

# 声明浏览器对象
from selenium import webdriver
from selenium.webdriver.common.by import By
'''

browser = webdriver.Chrome()
# browser=webdriver.Firefox()
# browser=webdriver.Edge()
# browser=webdriver.PhantomJS()
# browser=webdriver.Safari()


# 访问页面
browser.get('https://www.taobao.com')
# print(browser.page_source)#打印网页源代码

# 查找元素
# 一下三种方式相同
input_first = browser.find_element_by_id('q')
input_second = browser.find_element_by_css_selector('#q')
input_third = browser.find_element_by_xpath('//*[@id="q"]')
input_forth = browser.find_element(By.ID, 'q')
print(input_first)
print(input_second)
print(input_third)
print(input_forth)

print(10 * '-')
# 多个元素
# 筛选出service-bd li标签内容（返回一个list）
lis = browser.find_elements_by_css_selector('.service-bd li')
lis2 = browser.find_elements(By.CSS_SELECTOR, '.service-bd li')  # 同上
print(lis)
print(lis2)
browser.close()

print(10 * '-')
# 元素交互操作
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')  # 请求淘宝网
input = browser.find_element_by_id('q')  # 获取id为‘q’的内容（就是输入框）
input.send_keys('iPhone')  # 键入‘iPhone’
time.sleep(1)  # 休眠1s
input.clear()  # 清空文本
input.send_keys('iPad')  # 键入‘iPad’
button = browser.find_element_by_class_name('btn-search')  # 找到搜索按钮
button.click()  # 按下button
browser.close()

print(10 * '-')
# 交互动作
# 将动作附加到动作链中串行执行
from selenium.webdriver import ActionChains  # 导入动作链包

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)  # 发送请求
# 切换至iframe
browser.switch_to.frame('iframeResult')
# 找到拖拽包
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
# 声明动作链对象
actions = ActionChains(browser)
# 调用方法，把source拖拽到target
actions.drag_and_drop(source, target)
# perform执行动作
actions.perform()


print(10 * '-')
# 执行JavaScript
browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')
'''
'''
#获取元素信息
#获取属性
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
#得到包含logo信息的标签
logo = browser.find_element_by_id('zh-top-link-logo')
print(logo)
print(logo.get_attribute('class'))#输出logo的class属性
'''

'''
print(10 * '-')
# 获取文本值
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
# 按class名获取‘提问’标签
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.text)  # 输出标签文本内容
browser.close()

print(10 * '-')
# 获取ID、位置、标签名、大小
browser = webdriver.Chrome()
url = 'https://www.zhihu.com/explore'
browser.get(url)
input = browser.find_element_by_class_name('zu-top-add-question')
print(input.id)
print(input.location)
print(input.tag_name)
print(input.size)
browser.close()

print(10 * '-')
# Frame
# 相当于一个独立的网页（需要切换frame才能完成元素查找）
from selenium.common.exceptions import NoSuchElementException

browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')  # 切换到需要操作的frame
source = browser.find_element_by_css_selector('#draggable')  # 找出需要拖拽的对象
print(source)  # 打印出该对象
try:  # 在子frame里面尝试获取父frame的‘logo’元素
    logo = browser.find_element_by_class_name('logo')
except NoSuchElementException:  # 如果找不到‘logo’
    print('NO LOGO')
browser.switch_to.parent_frame()  # 切换到父frame
logo = browser.find_element_by_class_name('logo')  # 这下就可以找到了
print(logo)
print(logo.text)
browser.close()

print(10 * '-')
# 等待
# 隐式等待 如果加载出来就ok，没加载出来就等待10s，10s后还没加载出来就抛出异常
browser = webdriver.Chrome()
browser.implicitly_wait(10)  # 隐式等待10s
browser.get('https://www.zhihu.com/explore')
input = browser.find_element_by_class_name('zu-top-add-question')
print(input)
browser.close()

print(10 * '-')
# 显式等待 指定等待条件和最长等待时间，在最长等待时间内自动判断条件是否成立
# 若成立则立即返回
# 若不成立则一直等待 直到 最长等待时间，在改时间内成立则返回，不成立则抛出异常
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)  # 创建wait对象
# 判断元素是否已经出现
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# 判断元素是否可以点击
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)  # 返回
browser.close()

print(10 * '-')
# 前进后退
import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()
time.sleep(1)
browser.forward()
browser.close()


print(10 * '-')
#Cookies
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})#添加cookies
print(browser.get_cookies())
browser.delete_all_cookies()#删除所有cookies
print(browser.get_cookies())

'''

'''
print(10*"_")
#选项卡管理
import time
from selenium import webdriver
#通过js方式打开新的选项卡
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')#新建一个选项卡
print(browser.window_handles)#打印所有窗口的引用
#切换到第二个选项卡并打开淘宝网
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')#请求淘宝网
time.sleep(1)#睡眠一秒
#切换到第一个选项卡并打开python官网
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')#请求python官网

'''

'''
#异常处理
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

browser = webdriver.Chrome()
try:#超时报错
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:#找错
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('No Element')
finally:
    browser.close()
'''
