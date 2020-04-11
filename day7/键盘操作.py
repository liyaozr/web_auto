"""
============================
Author:luli
Time:2020/3/30
Company:Happy
============================
"""
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')

driver.implicitly_wait(30)

kw = driver.find_element_by_id('kw')
kw.send_keys('柠檬班')
kw.send_keys(Keys.ENTER)
# btn = driver.find_element_by_id('su')
# btn.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()
