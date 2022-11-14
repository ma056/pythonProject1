#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：wma
@Date    ：2022/7/1 3:43 PM
@process    :
@change :
'''
import requests
import pprint

url = 'https://vd.l.qq.com/proxyhttp'

data = {"buid":"vinfoad","adparam":"pf=in&ad_type=LD%7CKB%7CPVL&pf_ex=pc&url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fm441e3rjq9kwpsc%2Fh00251u5sdp.html&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fsearch%2F&ty=web&plugin=1.0.0&v=3.5.57&coverid=m441e3rjq9kwpsc&vid=h00251u5sdp&pt=&flowid=4edbb8b911552fe859ddcc9dca1c33d7_10201&vptag=m_v_qq_com%7Cvideolist%3Aclick&pu=2&chid=0&adaptor=2&dtype=1&live=0&resp_type=json&guid=58c04061fed6ba662bd7d4c4a7babf4f&req_type=1&from=0&appversion=1.0.174&uid=115600983&tkn=lGtJ5v2W_7pnTsuwhnFgKg.N&lt=qq&platform=10201&opid=03A0BB50713BC1C977C0F256056D2E36&atkn=75C3D1F2FFB4B3897DF78DB2CF27A207&appid=101483052&tpid=3&rfid=0c04189fe974e9f5eeb5ab41cbad09ba_1653140159","vinfoparam":"spsrt=1&charge=0&defaultfmt=auto&otype=ojson&guid=58c04061fed6ba662bd7d4c4a7babf4f&flowid=4edbb8b911552fe859ddcc9dca1c33d7_10201&platform=10201&sdtfrom=v1010&defnpayver=1&appVer=3.5.57&host=v.qq.com&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fm441e3rjq9kwpsc%2Fh00251u5sdp.html&refer=v.qq.com&sphttps=1&tm=1653140824&spwm=4&logintoken=%7B%22main_login%22%3A%22qq%22%2C%22openid%22%3A%2203A0BB50713BC1C977C0F256056D2E36%22%2C%22appid%22%3A%22101483052%22%2C%22access_token%22%3A%2275C3D1F2FFB4B3897DF78DB2CF27A207%22%2C%22vuserid%22%3A%22115600983%22%2C%22vusession%22%3A%22lGtJ5v2W_7pnTsuwhnFgKg.N%22%7D&vid=h00251u5sdp&defn=fhd&fhdswitch=0&show1080p=1&isHLS=1&dtype=3&sphls=2&spgzip=1&dlver=2&drm=32&hdcp=0&spau=1&spaudio=15&defsrc=2&encryptVer=9.1&cKey=PDUHac5qS3N6JZEItZs_lpJX5WB4a2CdS8kHyzIDVaqtHEZQ1c_W6myJ8hQFnmDDGMFrTtafKjvp2vPBr-xE-uhvZyEMY131vUh1H4pgCXe2Op9Lrzb_fbB32kFt6bl1q3wsEERWFNvMluNDEH6IC8EOljLQ2VfW2sTdospNPlD9535CNT9iSo3cLRH93ogtX_OJeYNVWrDYS8b5t1pjAAuGkoYGNScB_8lMah6WVCJtO-Ygxs9f-BtA8o_vOrSIjG_VH7z3tWJM-Px_AUNIsHEG9zgzglpES47qAUrvH-0706f5Jz35DBkQKl4XAh32cbzm4aSDFig3gLiesH-TyztJ3B01YYG7cwclU8WtX7G2Y6z8xdosNi5CqEttX-jHyd0GBgYGBgYFCmjn&fp2p=1&spadseg=3"}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
response = requests.get(url=url, json=data, headers=headers)
print(response.json())

import requests  # 发送请求
import re  # 正则
from tqdm import tqdm

# 伪装
# headers = {
#     # 身份信息
#     'cookie': 'pgv_pvid=7300130020; tvfe_boss_uuid=242c5295a1cb156d; appuser=BF299CB445E3A324; RK=6izJ0rkfNn; ptcz=622f5bd082de70e3e6e9a077923b48f72600cafd5e4b1e585e5f418570fa30fe; ptui_loginuin=1321228067; fqm_pvqid=89ea2cc7-6806-4091-989f-5bc2f2cdea5c; eas_sid=O1O654H4W3P8q7E5s3f8v1S5X1; LW_uid=31Q684N453P8R7C5w3k8k7v5a8; wxunionid=; wxopenid=; tmeLoginType=2; wxrefresh_token=; LW_sid=a1B6g46877j9D3t9d3l5x0B4K9; psrf_qqrefresh_token=6E3E1F0EA2B0A62D32794B915CC77053; psrf_qqopenid=4F37937E43ECA9EAB02F9E89BE1860E2; euin=oKoAoK-ANens7z**; psrf_qqunionid=FAEE1B5B10434CF5562642FABE749AB9; psrf_access_token_expiresAt=1657626768; psrf_qqaccess_token=D10984BFD6FA2D6CB2AED1B507B38B42; ufc=r24_1_1653029056_1652942836; o_cookie=3421355804; pgv_info=ssid=s5944849244; video_omgid=d91995430fa12ed8; vversion_name=8.2.95; Lturn=675; LKBturn=539; LPVLturn=28; LPLFturn=766; _qpsvr_localtk=0.8084329083292825; uid=169583373; lv_play_index=69; o_minduid=Mn7ZnxiFsdOwzWm3AW79de6jGhfswxd1; LPPBturn=973; LPSJturn=993; LVINturn=42; LPHLSturn=167; LZTturn=114',
#     # 浏览器基本信息
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'
# }
# data =data = '{"buid":"vinfoad","adparam":"pf=in&ad_type=LD%7CKB%7CPVL&pf_ex=pc&url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fm441e3rjq9kwpsc%2Fh00251u5sdp.html&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fsearch%2F&ty=web&plugin=1.0.0&v=3.5.57&coverid=m441e3rjq9kwpsc&vid=h00251u5sdp&pt=&flowid=4edbb8b911552fe859ddcc9dca1c33d7_10201&vptag=m_v_qq_com%7Cvideolist%3Aclick&pu=2&chid=0&adaptor=2&dtype=1&live=0&resp_type=json&guid=58c04061fed6ba662bd7d4c4a7babf4f&req_type=1&from=0&appversion=1.0.174&uid=115600983&tkn=lGtJ5v2W_7pnTsuwhnFgKg.N&lt=qq&platform=10201&opid=03A0BB50713BC1C977C0F256056D2E36&atkn=75C3D1F2FFB4B3897DF78DB2CF27A207&appid=101483052&tpid=3&rfid=0c04189fe974e9f5eeb5ab41cbad09ba_1653140159","vinfoparam":"spsrt=1&charge=0&defaultfmt=auto&otype=ojson&guid=58c04061fed6ba662bd7d4c4a7babf4f&flowid=4edbb8b911552fe859ddcc9dca1c33d7_10201&platform=10201&sdtfrom=v1010&defnpayver=1&appVer=3.5.57&host=v.qq.com&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fm441e3rjq9kwpsc%2Fh00251u5sdp.html&refer=v.qq.com&sphttps=1&tm=1653140824&spwm=4&logintoken=%7B%22main_login%22%3A%22qq%22%2C%22openid%22%3A%2203A0BB50713BC1C977C0F256056D2E36%22%2C%22appid%22%3A%22101483052%22%2C%22access_token%22%3A%2275C3D1F2FFB4B3897DF78DB2CF27A207%22%2C%22vuserid%22%3A%22115600983%22%2C%22vusession%22%3A%22lGtJ5v2W_7pnTsuwhnFgKg.N%22%7D&vid=h00251u5sdp&defn=fhd&fhdswitch=0&show1080p=1&isHLS=1&dtype=3&sphls=2&spgzip=1&dlver=2&drm=32&hdcp=0&spau=1&spaudio=15&defsrc=2&encryptVer=9.1&cKey=PDUHac5qS3N6JZEItZs_lpJX5WB4a2CdS8kHyzIDVaqtHEZQ1c_W6myJ8hQFnmDDGMFrTtafKjvp2vPBr-xE-uhvZyEMY131vUh1H4pgCXe2Op9Lrzb_fbB32kFt6bl1q3wsEERWFNvMluNDEH6IC8EOljLQ2VfW2sTdospNPlD9535CNT9iSo3cLRH93ogtX_OJeYNVWrDYS8b5t1pjAAuGkoYGNScB_8lMah6WVCJtO-Ygxs9f-BtA8o_vOrSIjG_VH7z3tWJM-Px_AUNIsHEG9zgzglpES47qAUrvH-0706f5Jz35DBkQKl4XAh32cbzm4aSDFig3gLiesH-TyztJ3B01YYG7cwclU8WtX7G2Y6z8xdosNi5CqEttX-jHyd0GBgYGBgYFCmjn&fp2p=1&spadseg=3"}'
# url = 'https://vd.l.qq.com/proxyhttp'
#
# response = requests.post(url=url, data=data, headers=headers)
# html_data = response.json()['vinfo']
# # m3u8_url = re.findall('url(.*?),',html_data)[3].split('"')[2]
# print(html_data)
# vinfo = eval(vinfom3u8=vinfo['vl']['vi'][0]['ul']['m3u8'])
# ts_list = re.sub('#E.*', '', m3u8)
# ts_list = ts_list.split()
# for ts in tqdm(ts_list):
#     ts_url = 'https://apd-abb582ce5099bda14af624ed12e9de7e.v.smtcdns.com/moviets.tc.qq.com/AMj691pA8OCTuBmUCFDH5yLIZZDMoeQbqI4-6zZUCHvs/uwMROfz2r5xgoaQXGdGnC2df64gVTKzl5C_X6A3JOVT0QIb-/PREasWbKzb39HD1GdIk3WV6hi3s1oVIUTqc1sPy7cIJqQYT52_Pm4YvgT9wqG94cOOMztqn5CJMq11YNY2nySMIWZO4cKzUV2H-qsrkw6DmtXHy9PZc6itf5qu1pKsrW2yBnESUygH2fEl1tM7-gCimuMLSEM-V-MJJdARp6w0QZmnjjm9hi2Q/' + ts
#     # 4. 保存数据
#     ts_data = requests.get(url=ts_url).content
#     # '斗罗大陆.mp4': 文件名
#     # 保存数据方式: 追加保存 以二进制方式
#     # as f: 文件取一个别名
#     with open('斗罗大陆.mp4', mode='ab') as f:
#         f.write(ts_data)
