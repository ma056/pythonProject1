#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/6/29 2:15 PM 
@process    :
pip install requests 数据请求
pip install parsel  数据解析模块
一、数据来源分析
分析之后的结果：
    1、先获取所有榜单的url地址
    2、获取所有歌曲的hash id参数
    3、把参数传入音乐数据包里面 获取音乐的url地址以及标题
    4、保存数据
二、代码实现步骤
    1、发送请求，对于榜单url地址发送请求
    2、获取数据，获取服务器返回的响应地址
    3、解析数据，提取榜单url地址发送请求
    4、发送请求，对于榜单url地址发送请求
    5、获取数据，获取服务器返回的响应数据
    6、解析数据, 提取我们想要 音乐 hash id 这两个参数
    7. 发送请求, 对于音乐数据包发送请求
    8. 获取数据, 获取服务器返回的数据内容
    9. 解析数据, 提取我们想要音乐标题 以及 音频播放地址
    10. 保存数据

@change :
'''
import re
import parsel   #数据解析模快
import requests
import os

def get_response(html_url):
    '''发送请求'''
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.get(url=html_url, headers=headers)
    return response


def get_list_url(html_url):
    '''获取榜单url地址'''
    response = get_response(html_url)
    selector = parsel.Selector(response.text)
    list_name_list = selector.css('.pc_rank_sidebar li a::attr(title)').getall()
    href = selector.css('.pc_rank_sidebar li a::attr(href)').getall()
    list_info = zip(list_name_list, href)
    # list_url = re.findall('<a title="(.*?)"  hidefocus="true" href="(.*?)"', response.text)
    return list_info


def get_music_id(html_url):
    '''获取音乐的hash ID参数'''
    response = get_response(html_url)
    print(response.text)
    Hash_list = re.findall('"Hash":"(.*?)"', response.text)
    album_id_list = re.findall('"album_id":(\d+),', response.text)
    music_id_list = zip(Hash_list, album_id_list)
    return music_id_list


def get_music_info(Hash, music_id):
    '''获取音乐url以及音乐标题'''
    link_url = f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={Hash}&dfid=3x7xDo1us1Te4bnL4J1NPACl&appid=1014&mid=9eaf1d946470b7babb8a25e05c76ba9c&platid=4&album_id={music_id}&_=1656656737012'
    response = get_response(html_url=link_url)
    title = response.json()['data']['audio_name']
    play_url = response.json()['data']['play_url']
    music_info = [title, play_url]
    return music_info


def save(title, play_url):
    '''保存数据'''
    music_content = get_response(html_url=play_url).content  # \获取音乐二进制数据
    os.makedirs('music', exist_ok=True)
    with open('music/' + title + '.mp3', mode='wb') as f:
        f.write(music_content)


def main(html_url):
    list_url = get_list_url(html_url)
    for list_name, link in list_url:
        # print(list_name,link)
        # print(f'------正在爬取{list_name}----------')
        music_id_list = get_music_id(html_url=link)
        for Hash, music_id in music_id_list:
            music_info = get_music_info(Hash, music_id)
            save(music_info[0], music_info[1])


if __name__ == '__main__':
    url = 'https://www.kugou.com/yy/html/rank.html'
    main(url)
