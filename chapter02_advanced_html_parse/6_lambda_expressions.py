# -*- coding: utf-8 -*-
'''
Created on 2018年1月27日

@author: Jeff Yang
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
# 另外，除了BeautifulSoup，还可以使用lxml和html parser等库解析网页

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, 'html.parser')
# lambda表达式
# BeautifulSoup允许把特定函数类型当作findAll()函数的对象，唯一限制是这些函数必须把一个标签作为参数且返回布尔类型
# BeautifulSoup用这个函数评估它遇到的每个标签，把为True的标签保留
tags = soup.findAll(lambda tag: len(tag.attrs) == 2)  # 获取有两个属性的标签
# tag.attrs可以获取它的全部属性，返回一个字典对象，可以获取和操作这些属性，如：tag.attrs["src"]
for tag in tags:
    print(tag)
