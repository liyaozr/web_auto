"""
============================
Author:luli
Time:2020/3/25
Company:Happy
============================
"""

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver.implicitly_wait(30)
driver.get('https://www.baidu.com/')

kw = driver.find_element_by_id('kw')
kw.send_keys('柠檬班')

driver.find_element_by_id('su').click()

# txt_elm = driver.find_element_by_xpath("//a[contains(text(),'lemon.ke.qq.com')]")
# print(txt_elm)

wait = WebDriverWait(driver, 30, poll_frequency=0.5)
# 等待元素被加载
locator = ('xpath', '//a[contains(text(),"lemon.ke.qq.com")]')
element = wait.until(EC.presence_of_element_located(locator))

# 等待元素可见
# locator = ('xpath', '//a[contains(text(),"lemon.ke.qq.com")]')
# # element = wait.until(EC.visibility_of_element_located(locator))

# 等待元素可被点击
# locator = ('xpath', '//a[contains(text(),"lemon.ke.qq.com")]')
# element = wait.until(EC.element_to_be_clickable(locator))

# 切换到新窗口
# 1、点击之前先统计一次窗口的数量
windows = driver.window_handles
# 2、操作点击
element.click()
# 3、判断是否满足切换条件
wait.until(EC.new_window_is_opened(windows))
# 4、切换到新窗口
driver.switch_to.window(driver.window_handles[-1])

# 检查一下新窗口有没有切换成功
huahua = driver.find_element_by_xpath('//h4[text()="华华老师"]')
huahua.click()
