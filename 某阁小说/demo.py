#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/7/5 5:32 PM 
@process    :
@change :
'''
import requests
import parsel

url = 'https://www.biqugee.com/book/60741/'
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
# print(response.text)
selector = parsel.Selector(response.text)
novel_name = selector.css('#info h1::text').get()  # 小说名字
href = selector.css('#list dd a::attr(href)').getall()  # 章节url
for link in href:
    link_url = f'https://www.biqugee.com{link}'
    print(link_url)
    response1 = requests.get(url=link_url)
    print(response1)
    selector1 = parsel.Selector(response1.text)
    title = selector1.css('.bookname h1::text').get()  # class是. id是#    章节名字
    content_list = selector1.css('#content::text').getall()
    content = '\n'.join(content_list)
    with open(novel_name + '.txt', mode='a', encoding='utf-8') as f:
        f.write(title)
        f.write('\n')
        f.write(content)
        f.write('\n')
    print(title)
