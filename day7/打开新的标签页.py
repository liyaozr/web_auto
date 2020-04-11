"""
============================
Author:luli
Time:2020/4/2
Company:Happy
============================
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.12306.cn/index/")

# 打开，新窗口
driver.execute_script("window.open();")
