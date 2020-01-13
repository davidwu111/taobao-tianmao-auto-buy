# python3.6.5
# coding:utf-8

"""
@time:2019-02-16 16:50
@原作者author: 李铭

@2019-11-08 10:35
@改写：saul

@2020-01-13 20:40
@改写:David Wu

程序利用自动测试工具模拟用户下单操作，完成商品的抢购
仅作为学习过程中的实践，无商业用途
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ex
import datetime
import time
from urllib.parse import urlparse


# def password_login():
#     # Login directly by username and password. Unable to bypass verification. Give up by now.
#     driver.get('https://login.taobao.com/member/login.jhtml')
#     time.sleep(5)
#     input_page = driver.find_element_by_id('J_Quick2Static')
#     input_page.click()
#     time.sleep(2)
#     user_name = ''
#     password = ''
#     input_user = driver.find_element_by_id('TPL_username_1')
#     input_pwd = driver.find_element_by_id('TPL_password_1')
#     input_user.send_keys(user_name)
#     input_pwd.send_keys(password)
#     time.sleep(5)
#     input_login = driver.find_element_by_id('J_SubmitStatic')
#     input_login.click()
#     wait = WebDriverWait(driver, 10)
#     wait.until(ex.presence_of_all_elements_located((By.ID, 'content_left')))


def login(_url, _mall):
    """
    登陆函数

    _url:商品的链接
    _mall：商城类别
    """
    # password_login()
    driver.get(_url)
    driver.implicitly_wait(10)
    time.sleep(5)
    # 淘宝和天猫的登陆链接文字不同
    if _mall == '1':
        # 找到并点击淘宝的登陆按钮
        driver.find_element_by_link_text("亲，请登录").click()

    else:
        # 找到并点击天猫的登陆按钮
        driver.find_element_by_link_text("请登录").click()
    print("请在30秒内完成登录,")
    # 用户扫码登陆
    time.sleep(30)


def buy(buy_time, _mall):
    """
    购买函数

    buy_time:购买时间
    mall:商城类别

    获取页面元素的方法有很多，获取得快速准确又是程序的关键
    在写代码的时候运行测试了很多次，css_selector的方式表现最佳
    """
    if _mall == '1':
        # "立即购买"的css_selector
        btn_buy = '#J_juValid > div.tb-btn-buy > a'
        # "立即下单"的css_selector
        btn_order = '#submitOrderPC_1 > div.wrapper > a'
        # 提交订单按钮有变化,增加了'PC'
    else:
        btn_buy = '#J_LinkBuy'
        btn_order = '#submitOrderPC_1 > div > a'
        # 提交订单按钮有变化,增加了'PC'
    while True:
        # 现在时间大于预设时间则开售抢购
        if datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') > buy_time:
            try:
                # 找到“立即购买”，点击
                if driver.find_element_by_css_selector(btn_buy):
                    driver.find_element_by_css_selector(btn_buy).click()
                    print("生成订单")
                    break
                time.sleep(2)
                # 等待时间缩短至10ms，下同
            except:
                time.sleep(2)
        # print ('还在试，别催了')

    while True:
        try:
            # 找到“立即下单”，点击，
            if driver.find_element_by_css_selector(btn_order):
                driver.find_element_by_css_selector(btn_order).click()
                # 下单成功，跳转至支付页面
                print("购买成功")
                break
        except:
            time.sleep(2)


# Check if URL contains string 'tmall'
def check_mall(_url):
    parse_result = urlparse(_url)
    domain = parse_result.netloc
    if domain.find('tmall') > 1:
        return 2
    else:
        return 1


if __name__ == "__main__":
    # url=input("请输入商品链接:")
    # mall=input("请选择商城（淘宝 1  天猫 2  输入数字即可）： ")
    # bt=input("请输入开售时间【2019-02-15（空格）12:55:50】")
    url = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.92.395c318cR7BQNr&id=606633567102&ns=1&abbucket=16&skuId=4461849831762'
    # 命令行粘贴不便，还是在源代码直接输入吧
    mall = check_mall(url)
    # 同上，2是天猫，1是淘宝
    bt = '2020-01-13 22:49:00'
    # 同上，时间自己改
    bt_dt = datetime.datetime.strptime(bt, '%Y-%m-%d %H:%M:%S')
    now_dt = datetime.datetime.now()
    print("还有%.1f小时，要开始么？" % ((bt_dt - now_dt).seconds / 3600))
    input()  # 随便说点啥，就要正式开始了
    # 允许浏览器重定向，Framebusting requires same-origin or a user gesture

    chrome_options = Options()
    chrome_options.add_argument("disable-web-security")
    # 创建浏览器对象
    driver = webdriver.Chrome(options=chrome_options)
    # 窗口最大化显示
    driver.maximize_window()

    login(url, mall)
    buy(bt, mall)
