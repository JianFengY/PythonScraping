# -*- coding: utf-8 -*-
'''
Created on 2018年1月27日

@author: Jeff Yang
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re  # 正则表达式

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, 'html.parser')
# <img src="../img/gifts/img1.jpg">
# .匹配任意单个字符、*匹配0次或多次、+匹配至少一次
images = soup.findAll("img", {"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])
