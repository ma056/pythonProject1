# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : wordcount_summary_view.py
@Author : wenjing
@Date : 2022/12/1 9:30
"""
lst = [{'level': 19, 'star': 36, 'time': 2},
       {'level': 20, 'star': 40, 'time': 1}]
# lst.sort(key=lambda k: (k.get('time', 0)))
# lst.sort(key=lambda x: x.get('time'))
a = sorted(lst,key=lambda x:x.get('time'))
print(a)
