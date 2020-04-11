"""
============================
Author:luli
Time:2020/3/27
Company:Happy
============================
"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(15)

# 定位设置
set_ele = driver.find_element_by_xpath("//div[@id='u1']/a[@name='tj_settingicon']")
# 鼠标移动到设置按钮
action = ActionChains(driver)
action.move_to_element(set_ele)
# 关键，一定要执行
action.perform()

# 定位高级搜索
driver.find_element_by_xpath("//a[contains(@href,'gaoji/advanced')]").click()

# 定位到下拉列表
option = driver.find_element_by_xpath("//option[.='最近一天']")
# 点击
option.click()

# 定位到下拉列表
s_elem = driver.find_element_by_xpath("//select[@name='ft']")
select = Select(s_elem)
select.select_by_value('pdf')

time.sleep(5)
driver.quit()
