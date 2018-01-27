# -*- coding: utf-8 -*-
'''
Created on 2018年1月27日

@author: Jeff Yang
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, 'html.parser')
# .parent选取父标签而.parents选取所有的父辈节点
print(soup.find("img", {"src":"../img/gifts/img1.jpg"
    }).parent.previous_sibling.get_text())
