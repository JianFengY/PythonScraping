# -*- coding: utf-8 -*-
'''
Created on 2018年1月26日

@author: Jeff Yang
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
# print(type(html))  # <class 'http.client.HTTPResponse'>对象
# print(type(html.read()))  # <class 'bytes'>，网页源码
soup = BeautifulSoup(html, 'html.parser')  # html.read()和html都可以？
# soup.tagname只能获取第一个指定的标签
# findAll()可以获取所有指定标签
names = soup.findAll("span", {"class":"green"})
# find_all(name, attrs, recursive, text, limit)
# find(name, attrs, recursive, text)
# name为标签名，可传递一个标签名称或多个标签名称组成的列表做参数，如.findAll({"h1","h2","h3"})
# attrs是用一个用字典封装一个标签的若干属性和对应属性值，如.findAll("span", {"class":{"green", "red"}})
# recursive是个布尔值，True会查找标签参数的所有子标签以及子标签的子标签，False只会查找一级标签。一般不需要设置
# text是用标签的文本内容匹配而非属性，如.findAll(text="example")
# limit，限制条数，find实际上是find_all的limit等于1的情况
# 还有一个keyword参数，实际上是冗余功能，如.findAll(id="text")与.findAll("",{"id":"text"})相同
# 且keyword用到class时要写成class_
for name in names:
    # get_text()返回只包含标签的内容的字符串，不包括标签，通常打印存储和操作数据时，最后才使用get_text()，应尽可能保留标签结构
    print(name.get_text())

allText = soup.findAll(id="text")
print(allText[0].get_text())

# BeautifulSoup库里的对象：
# BeautifulSoup对象，即前面的soup
# 标签Tag对象：BeautifulSoup对象使用find()和findAll()或使用子标签获取的单个或一列对象
# NavigableString对象：表示标签里的文字，不是标签，有些函数和操作能生成NavigableString对象
# Comment对象：用来查找html文档的注释标签，<!--像这样-->
