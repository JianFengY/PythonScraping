# -*- coding: utf-8 -*-
'''
Created on 2018年1月26日

@author: Jeff Yang
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, 'html.parser')
# children找出子标签，descendants找出所有后代标签
# 子标签是父标签的下一级，后代标签是一个父标签的所有下级标签
for child in soup.find("table", {"id":"giftList"}).children:
    print(child)
