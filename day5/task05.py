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
driver.implicitly_wait(30)
driver.get('https://ke.qq.com/')
driver.maximize_window()

# 点击登陆按钮
driver.find_element_by_id('js_login').click()
# 点击QQ登陆
driver.find_element_by_xpath("//a[contains(@class,'btns-enter-qq')]").click()
# 设置等待
wait = WebDriverWait(driver, 30)
locator = ('name', 'login_frame_qq')
wait.until(EC.frame_to_be_available_and_switch_to_it(locator))

# 点击账号密码登陆
driver.find_element_by_id('switcher_plogin').click()
# 输入用户名和密码
user = driver.find_element_by_id('u')
pwd = driver.find_element_by_id('p')
# 用户名和密码换一下哦
user.send_keys('aa')
pwd.send_keys('bb.')
# 点击登录按钮
driver.find_element_by_id('login_button').click()

# driver.quit()
