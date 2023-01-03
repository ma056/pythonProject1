# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 知识点.py
@Author : wenjing
@Date : 2022/12/28 13:34
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver.exe")
# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择time,sleep(2)
driver.get("http://www.baidu.com/")


kw = driver.find_element(By.CSS_SELECTOR, "#kw")
# kw是百度搜索输入框，输入字符串”长城
kw.send_keys("长城")
# id = 'su'是百度搜索按钮 .click() 是模拟点击
driver.find_element(By.CSS_SELECTOR, "#su").click()

# 1.元素定位
# 获取单个元素
driver.find_element(By.ID, "inputing")
driver.find_element(By.CSS_SELECTOR, "#inputing")
driver.find_element(By.TAG_NAME, "div")
driver.find_element(By.NAME, "username")
driver.find_element(By.LINK_TEXT, "下一页")

# 获取多个元素：find_elements
driver.find_elements(By.LINK_TEXT, "下一页")


# 2.若遇到有弹框阻碍到点击
# 先获取遮挡的广告条，点击关闭
close_btn = driver.find_elements(By.CSS_SELECTOR, ".guide-con .guide-close")
close_btn.click()
#在进行其他点击操作
XXX.click()


# 3.内容获取
'''
size                        返回元素大小
text                        获取元素的文本 <div>hello</div>
current_url                 获取当前页面url
get_attribute               获取属性值 <a href='xxx'>百度</a>
is_display()                判断元素是否可见
is_enabled()                判断元素是否可用
'''
# eg:
driver = webdriver.Chrome("./chromedriver.exe")
driver.get("https://fanyi.youdao.com/")
transmachine = driver.find_element(By.ID,"transMachine")
print(transmachine.size)
print(transmachine.text)
print(transmachine.get_attribute('href'))
print(transmachine.is_displayed())
print(transmachine.is_enabled())


# 窗口操作
'''
maximize_window()  最大化窗口
set_window_size(100,100)    设置浏览器大小
set_window_position         浏览器位置
'''