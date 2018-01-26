# -*- coding: utf-8 -*-
'''
Created on 2018年1月26日

@author: Jeff Yang
'''

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup


def getTitle(url):
    """获取title"""
    try:
        # 网页在服务器上不存在或获取页面出现错误会返回404、500等HTTP错误，抛出HTTPError
        # 服务器不存在（url打不开）或url写错了，urlopen()返回一个None对象
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')  # 把html内容传到BeautifulSoup对象
        # 如果调用的标签不存在BeautifulSoup就返回None对象，如果调用这个None对象的子标签会发生AttributeError
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

        
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found!")
else:
    print(title)
