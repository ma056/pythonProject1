# -- coding: utf-8 --
"""
@Project : pythonProject1
@File : 当当网.py
@Author : wenjing
@Date : 2022/12/28 16:54
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver.exe")

# 隐士等待，30秒有加载元素就去等
driver.implicitly_wait(30)

driver.get("https://www.dangdang.com/")
key = driver.find_element(By.ID, "key_s")
key.send_keys('科幻')

search = driver.find_element(By.CSS_SELECTOR, ".search .button")
search.click()

for i in range(5):
    shoplist = driver.find_elements(By.CSS_SELECTOR, '.shoplist li')
    for li in shoplist:
        print(li.find_element(By.CSS_SELECTOR, 'a').get_attribute('title'))

    next = driver.find_element(By.LINK_TEXT, '下一页')
    next.click()
