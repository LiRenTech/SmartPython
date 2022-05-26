# -*- encoding: utf-8 -*-
"""
PyCharm videoBarrage
弹幕分析
2022年05月23日
by littlefean
"""
import os
from typing import *
import matplotlib.pyplot as plt
# https://www.bilibili.com/read/cv14913712/  如何爬弹幕
# https://comment.bilibili.com/{720382441}.xml
import requests
from bs4 import BeautifulSoup
import jieba
from wordcloud import WordCloud
# from pyecharts.charts import WordCloud
from collections import Counter

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}
exclude = {
    '我们', '你们', '他们', '它们', '因为', '因而', '所以', '如果', '那么',
    '如此', '只是', '但是', '就是', '这是', '那是', '而是', '而且', '虽然',
    '这些', '有些', '然后', '已经', '于是', '一种', '一个', '一样', '时候',
    '没有', '什么', '这样', '这种', '这里', '不会', '一些', '这个', '仍然', '不是',
}


def stringToList(string):
    """将xml内部字符串分词成一个列表"""
    # string.encoding = string.apparent_encoding
    soup = BeautifulSoup(string, "lxml")
    content_all = soup.find_all("d")

    # 分词
    wordList = []
    for content in content_all:
        wordList += jieba.lcut(content.string)
    return wordList


def saveVideoWordCloud(videoAid: int, saveName: str):
    url = f"https://comment.bilibili.com/{videoAid}.xml"
    res = requests.get(url, headers=headers)
    wordList = stringToList(res)
    wordDict = Counter(wordList)

    # 词云可视化
    wordCloud = WordCloud()
    wordCloud.add(series_name="", data_pair=list(wordDict.items()), word_size_range=[20, 80])
    wordCloud.render(f"{saveName}.html")
    return None


def main():
    # saveVideoWordCloud(720382441, "python迷惑行为：我自己写我自己")
    # saveVideoWordCloud(939151141, "【python技巧014】用deque替代list做广度优先遍历")
    # saveVideoWordCloud(939083967, "【python技巧013】用Counter做元素统计")
    # saveVideoWordCloud(256448723, "python迷惑行为：我给你我自己")
    lst = []
    for item in os.listdir("inputData\\弹幕源文件"):
        print(item)
        with open("inputData\\弹幕源文件" + os.sep + item, encoding="utf-8") as f:
            lst += stringToList(f.read())
    dic = Counter(lst)
    # lst 过滤
    newLst = []
    for item in lst:
        if item in exclude:
            continue
        else:
            newLst.append(item)
    lst = newLst
    # print(dic)
    for k, v in dic.items():
        print(k, "\t", v)

    wc = WordCloud(width=1920, height=1080,
                   stopwords=exclude,
                   font_path=r'C:\Users\20281\AppData\Local\Microsoft\Windows\Fonts\STXIHEI.TTF').generate(
        " ".join(lst))
    # plt.imshow(wc, interpolation='bilinear')
    # plt.axis('off')
    # plt.show()
    wc.to_file("outputData\\out1.png")
    return None


if __name__ == "__main__":
    main()
