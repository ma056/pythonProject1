# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : xpath实战.py
@Author : wenjing
@Date : 2022/12/7 15:45
 pip install lxml
"""
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}
response = requests.get('https://www.douguo.com/jingxuan/0', headers=headers)
# 为了写xpath内容，我们先将内容保存到本地，然后爬取多页内容
with open('jingxuan.html', 'wb') as stream:
    stream.write(response.content)

##1.获取美食的详情页链接
### xptah==》 //ul[@id='jxlist']/li/a/@href
with open('jingxuan.html', 'r') as stream:
    all = stream.read()
    html = etree.HTML(all)
    links = html.xpath('//ul[@id="jxlist"]/li/a/@href')
    print(links)

## 2.美食图片的获取，美食图片的链接在a标签的img标签中
### //ul[@id='jxlist]/li/div/a/img/@src

## 3. 菜名的获取
### //ul[@id='jxlist']/li/div/a[1]/text()       这里的1指的就是第一个a标签

## 4.发表用户的获取
### //ul[@id = 'jxlist']/li/div/a/img/@alt
import re

users = html.xpath('//ul[@id="jxlist"]/li/div/a[2]/text()')
pattern = re.compile(r"\n+|\s+", re.S)  # 查找\n和\s进行替换
users = [pattern.sub('', users[u]) for u in range(1, len(users), 2)]  # 删除第一个空内容print(users)

## 5.浏览量和收藏量的获取方式是一样的，分别在两个span标签中
### //ul[@id='jxlist']/li/div/span/text()
