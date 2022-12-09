# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : xpath知识点.py
@Author : wenjing
@Date : 2022/12/7 16:01

# 字母：string.ascii_letters

# 大写：string.ascii_uppercase

# 小写：string.ascii_lowercase
"""
# xpath可以使用路径表达式在XML上选取节点，从而达到确认元素的目的，我们先来介绍以下语法规则。


'''
语法规则
表达式	作用
nodename	选取此层级节点下的所有子节点
/	代表从根节点进行选取
//	可以理解为匹配，就是在所有节点中选取此节点，直到匹配为止
.	选取当前节点
…	选取当前节点上一层（上一级目录）
@	选取属性（也是匹配）
'''

'''
标签定位
方式	效果
/html/body/div	表示从根节点开始寻找，标签与标签之间/表示一个层级
/html//div	表示多个层级 作用于两个标签之间（也可以理解为在html下进行匹配寻找标签div）
//div	从任意节点开始寻找，也就是查找所有的div标签
./div	表示从当前的标签开始寻找div
'''

'''
属性定位
需求	格式
定位div中属性名为href，属性值为‘www.baidu.com’的div标签	@属性名=属性值
href为属性名 'www.baidu.com’为属性值	/html/body/div[href=‘www.baidu.com’]
'''

'''
索引定位
需求	格式
定位ul下第二个li标签(下图)	//ul/li[2]
索引值开始位置为	1
'''

'''
取文本内容
方法	效果
/text()	获取标签下直系的标签内容
//text()	获取标签中所有的文本内容
string()	获取标签中所有的文本内容
'''