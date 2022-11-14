#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/7/11 11:09 AM 
@process    :
@change :
一：数据来源：
    需求：输入出发地-目的地 时间 就可以实现登录
    通过开发者工具进行抓包分析
'''
import requests
import pandas as pd
import json
f = open('city.json', mode='r', encoding='utf-8')
text = f.read()
city_json = json.loads(text)
# dit = dict(text)
# <class 'str'>   字符串转字典 json
while True:
    from_station = input('请输入出发的城市: ')
    to_station = input('请输入目的城市: ')
    date = input('请输入查询时间(格式: 2021-09-10):  ')
    url = r'https://kyfw.12306.cn/otn/leftTicket/query'
    data = {
        "leftTicketDTO.train_date": "2022-07-11",
        'leftTicketDTO.from_station': city_json[from_station],
        'leftTicketDTO.to_station': city_json[to_station],
        "purpose_codes": "ADULT",
    }
    headers = {
        "Cookie": "JSESSIONID=0A60948F469447A95EB75F71F49506E5; BIGipServerotn=1307574794.24610.0000; BIGipServerpool_passport=132383242.50215.0000; RAIL_EXPIRATION=1657816485201; RAIL_DEVICEID=NbX0NPBU7wRAcQl4arxEV5pdJb2qyCmO85wT9nF51hhpZvFeRIQ4ZpH2ZzHiTAXssN5uyOQVWEiuAVGDoe41gHCnijm25PaDrjywYf7ItuAWLidDnUx9sBRXE9LfedqVXz9lktQZU8yQ5Ci1al2J7Myw0yR4f51T; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u957F%u6C99%2CCSQ; _jc_save_fromDate=2022-07-11; _jc_save_toDate=2022-07-11; _jc_save_wfdc_flag=dc",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }
    response = requests.get(url=url, params=data, headers=headers)
    # <Response [200]> 返回的是响应体对象
    # response.text  获取响应体的文本数据
    # response.json() 获取响应体json形式
    response.encoding = response.apparent_encoding  # 自动识别编码
    # print(response.json())
    result = response.json()['data']['result']
    lis = []
    for index in result[1:]:
        # 字符串分割方法
        index_list = index.replace('有', 'Yes').replace('无', 'No').split('|') # 返回的列表 可以根据索引位置提取内容
        page = 0
        Num = index_list[3] # 车次
        time_1 = index_list[8] # 发车时间
        time_2 = index_list[9] # 到达时间
        prince_seat = index_list[32]  # 特等座
        first_class_seat = index_list[31]  # 一等座
        second_class = index_list[30]  # 二等座
        Wz = index_list[26] # 无座
        Yz = index_list[29]  # 硬座
        Rw = index_list[23] # 软卧
        Yw = index_list[28] # 硬卧
        dit = {
            'Num': Num,
            'Start': time_1,
            'End': time_2,
            'Top':prince_seat,
            'First':first_class_seat,
            'Second':second_class,
            'Wz': Wz,
            'Yz': Yz,
            'Rw': Rw,
            'Yw': Yw,
        }
        lis.append(dit)
        print(dit)
        # break
    pd.set_option('display.max_rows', None)
    columns = ['Num', 'Start', 'End', 'Top', 'First', 'Second', 'Yz', 'Wz', 'Rw', 'Yw']
    content = pd.DataFrame(lis, columns=columns)
    print(content)

