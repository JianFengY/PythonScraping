# -*- coding: utf-8 -*-
'''
Created on 2018年1月26日

@author: Jeff Yang
'''

# 从urllib库的request模块导入urlopen函数
# urllib是标准库，不用额外安装，包含了从网络请求数据，处理cookies，改变请求头和用户代理这些元数据的函数
# urllib文档 https://docs.python.org/3/library/urllib.html
from urllib.request import urlopen
# python2里的urllib2库在python3里改名为urllib，被分成一些子模块urllib.request,urllib.parse,urllib.error等

# urlopen()用来打开并读取一个从网络获取的远程对象，可以读取html文件，图像文件或其它任何文件流
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())
