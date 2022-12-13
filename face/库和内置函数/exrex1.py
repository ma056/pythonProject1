# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : exrex1.py
@Author : wenjing
@Date : 2022/12/13 11:04
"""
## https://github.com/asciimoo/exrex
## https://exrex.readthedocs.io/en/latest/#
import exrex

for i in range(5):
    # 手机号码格式
    rule = r"^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$"
    phone_number_str = exrex.getone(rule)
    print(phone_number_str)