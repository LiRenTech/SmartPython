# -*- encoding: utf-8 -*-
"""
PyCharm htmlGetter
2021年10月22日
by littlefean
"""
from time import sleep

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from selenium import webdriver

# 忽略requests证书警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class HtmlGetter:
    def __init__(self, url: str, encode="", decode=""):
        self.url = url
        self.decode = decode
        self.encode = encode

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }

    def get(self):
        """以普通的爬虫方式获取这个网页的内容"""
        try:
            response = requests.get(self.url, headers=self.headers, verify=False)
            html = response.text
            # html = html.encode("ISO-8859-1")
            # html = html.decode("utf-8")
            if self.encode != "":
                html = html.encode(self.encode)
            if self.decode != "":
                html = html.decode(self.decode)
            return html
        except ConnectionError:
            print(f"这个网站{self.url}无法连接")
            return "<html></html>"
        except requests.exceptions.ConnectionError:
            print(f"这个网站{self.url}连接超时")
            return "<html></html>"
        except Exception as e:
            print(f"访问这个网站出现了{e}错误。Exception异常捕获")
            return "<html></html>"

    def dynamicGet(self):
        """
        以动态网页的方式获取这个网站的内容
        禁止打印太多信息 https://blog.csdn.net/wm9028/article/details/107536929
        """
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
        browser.get(self.url)
        res = browser.page_source
        browser.quit()
        sleep(1)
        return res


def htmlGetterZ(function):
    """一个函数装饰器，用于把函数装饰成无论如何都能够执行下去的样子
    为了不影响后面函数继续运行"""

    def newFunc(*args, **kwargs):
        def printError(mark: str):
            print(f"发生了错误，函数：{function.__name__}{args}, {kwargs}错误类型：【{mark}】")

        try:
            function(*args, **kwargs)
        except FileNotFoundError:
            printError("FileNotFoundError")
        except IOError:
            printError("IOError")
        except IndexError:
            printError("索引错误IndexError")
        except ValueError:
            printError("值类型错误ValueError")
        except Exception as e:
            printError(str(e))

    return newFunc
