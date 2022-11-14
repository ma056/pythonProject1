#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/6/28 4:50 PM 
@process    :
@change :
'''
import re
import requests
import os

# 若想爬其他榜单，只需要更改url中的id
url = 'https://music.163.com/discover/toplist?id=3778678'
# headers 请求头，就是用伪装python代码的，把python代码伪装成浏览器对于服务器发送请求
# 服务器接收到请求之后，会给我们返回响应数据（response）
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
# <li><a href="/song?id=1824045033">再见莫妮卡</a>
html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>', response.text)
# 正则表达式提取出来的一个内容 返回是列表 里面每一个元素都是元组
save_path = 'music'  # 保存路径
os.makedirs(save_path, exist_ok=True)
for num_id, title in html_data:
    # https://music.163.com/song/media/outer/url?id=1859245776.mp3
    music_url = f'https://music.163.com/song/media/outer/url?id={num_id}.mp3'
    # 对于音乐播放地址发送请求，获取二进制数据内容
    music_content = requests.get(url=music_url, headers=headers).content
    with open(os.path.join(save_path, title) + '.mp3', mode='wb') as f:
        f.write(music_content)
    print(title)

