import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
from pyquery import PyQuery as pq
from config_taobao_food import *
import pymongo

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


# 打开Chromedriver的设置
options = webdriver.ChromeOptions()

# 不加载图片，加快访问速度
# options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

# 设置为开发者模式，防止被牛逼网站识别为Selenium
options.add_experimental_option('excludeSwitches', ['enable-automation'])

# 添加一个headers防止被识别为robot
# options.add_argument('User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')

# 创建一个Chrome浏览器
browser = webdriver.Chrome(chrome_options=options)  # 将设置配置进去
wait = WebDriverWait(browser, 10)  # 超时失常设定为10s


def log_in(user_name, pass_word):
    try:
        browser.get('https://login.taobao.com/member/login.jhtml',)
        # 等待并定位到“密码登录”选项
        try:
            password_login = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static')))
            password_login.click()  # 点击
        except ElementNotVisibleException:
            pass

        # 等待并定位到‘微博登录’选项
        weibo_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_OtherLogin > a.weibo-login')))
        weibo_login.click()  # 点击

        # 等待并定位到帐号输入框
        username_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(2) > div > input')))
        username_input.send_keys(user_name)  # 输入帐号

        # 等待并定位到密码输入框
        password_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(3) > div > input')))
        password_input.send_keys(pass_word)  # 输入密码

        # 等待并定位到登录按钮
        login_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(7) > div:nth-child(1) > a')))
        login_button.click()  # 点击登录

        # 直到获取到淘宝会员昵称才能确定是登录成功
        taobao_name = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a')))
        print('用户', taobao_name, '登录成功')  # 打印成功信息
    except TimeoutException:
        log_in(user_name, pass_word)


def search():  # 加载淘宝网页
    try:
        # 获取输入框
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#q')))
        # 获取搜索按钮
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm > div.search-button > button')))
        # 输入‘美食’内容
        input.send_keys('美食')
        # 点击搜索按钮
        submit.click()
        # 总页数
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.total')))
        get_products()  # 解析页面获取商品信息
        return total.text  # 返回总页数
    except TimeoutException:  # 如果超时，则重新请求一次（此处用递归方法）
        return search()


def next_page(page_number):
    try:
        # 获取输入页数的框
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input')))
        # 获取确定按钮
        submit = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()  # 清空输入框
        input.send_keys(page_number)  # 输入页数
        submit.click()  # 点击确定
        # 直到高亮的页码是当前输入页码
        wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'), str(page_number)))
        get_products()  # 解析页面获取商品信息
    except TimeoutException:  # 超时出错就重新调用
        next_page(page_number)


def main():
    # 账号密码
    username = '15216730181'
    password = 'QqhuanxiangQq123'
    log_in(username, password)  # 登录
    total = search()  # 获取总页数
    total = int(re.compile('(\d+)').search(total).group(1))  # 解析出总页数
    # print(total)
    for i in range(2, total + 1):
        next_page(i)  # 全自动翻页


def get_products():  # 解析页面获取商品信息
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

def save_to_mongo(result):
    try:
        if db[MONGO_TABLE].insert(result):
            print('存储到MONGODB成功',result)
    except Exception:
        print('存储到MONGODB失败', result)

if __name__ == '__main__':
    main()
