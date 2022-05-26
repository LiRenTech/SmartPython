# -*- encoding: utf-8 -*-
"""
PyCharm fansGetter
2022年05月23日
by littlefean
"""
from time import sleep
from typing import *

from selenium.webdriver import ActionChains

from htmlGetter import HtmlGetter
from selenium import webdriver
from bs4 import BeautifulSoup


def main():
    url = "https://space.bilibili.com/480804525/fans/fans"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 禁止打印日志
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 实现了规避监测
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless')  # 增加无界面选项
    chrome_options.add_argument('--disable-gpu')  # 如果不加这个选项，有时定位会出现问题
    chrome_options.add_argument('--start-maximized')  # 最大化
    chrome_options.add_argument('--incognito')  # 无痕隐身模式
    chrome_options.add_argument('log-level=3')  # INFO = 0 WARNING = 1 LOG_ERROR = 2 LOG_FATAL = 3 default is 0
    # 启动浏览器，获取网页源代码
    browser = webdriver.Chrome(chrome_options=chrome_options,
                               # executable_path='<path-to-chrome>',
                               # executable_path='',
                               # options=chrome_options
                               )
    browser.get(url)

    # be-pager-next 是下一页的按钮

    def getFansList(string):
        """通过html字符串来获取列表 粉丝列表"""
        soup = BeautifulSoup(string, "lxml")
        arr = soup.select(".list-item")
        resLst = []
        for item in arr:
            title = item.select("p")[0].string.strip()
            if title == "这个人没有填简介啊~~~":
                title = ""
            name = item.select(".fans-name")[0].string.strip()
            # print(title, end="\n\n")
            # print(name, end="\n\n")
            user = {"title": title, "name": name}
            resLst.append(user)
        return resLst

    print(browser.page_source)

    print("-" * 10)
    lst = []

    ac = ActionChains(browser)

    for i in range(1, 131 + 1):
        lst += getFansList(browser.page_source)
        print(lst)
        # 点击下一个
        ele = browser.find_element_by_class_name("space_input")
        # ele = browser.find_element_by_class_name("be-pager-next").find_element_by_tag_name("a")
        print(ele)
        browser.implicitly_wait(10)

        # ac.move_to_element(ele).perform()
        # ac.click(ele).perform()
        # ele.click()
        search_text = ele.send_keys(str(i))
        search_text.submit()
        print(i)

    browser.quit()
    """
    selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element <a>...</a> is not clickable at point (758, 571). Other element would receive the click: <div class="modal-mask"></div>
  (Session info: headless chrome=97.0.4692.71)
  
  selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable:  has no size and location
  (Session info: headless chrome=97.0.4692.71)
    """
    return None


if __name__ == "__main__":
    main()
