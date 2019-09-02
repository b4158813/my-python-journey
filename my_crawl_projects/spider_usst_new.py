import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


def log_in(username, password):
    try:
        browser.get('http://jwgl.usst.edu.cn/jwglxt/xtgl/index_initMenu.html')
        username_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#yhm')))
        username_input.send_keys(username)

        password_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mm')))
        password_input.send_keys(password)

        login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#dl')))
        login_button.click()

        login_confirm = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#drop1')))
        print('登录成功！')
    except TimeoutException:
        log_in(username, password)

def main():
    username = '1711410424'
    password = 'QqhuanxiangQq123'
    log_in(username,password)


if __name__ == '__main__':
    main()
