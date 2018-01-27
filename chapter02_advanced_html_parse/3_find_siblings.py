# -*- coding: utf-8 -*-
'''
Created on 2018年1月26日

@author: Jeff Yang
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
soup = BeautifulSoup(html, 'html.parser')
# .tr找到第一个tr，之后.next_siblings找到这个tr后面的所有兄弟标签，返回值不包括这个tr
# 即使只有一个table，也最好带上标签的属性是选择更具体
# 相应的有previous_siblings找出前面的所有兄弟标签
# 还有next_sibling、previous_sibling分别返回后一个和前一个的单个兄弟标签
for sibling in soup.find("table", {"id":"giftList"}).tr.next_siblings:
    print(sibling)
