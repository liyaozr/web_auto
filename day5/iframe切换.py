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
driver.get('http://localhost:63342/web_auto/day5/iframe_demo.html?_ijt=j84c291ib7943970tkfhac160r')

wait = WebDriverWait(driver, 30)
# 1、id
# 2、name
# 3、WebElement
# 4、xpath
locator = ('id', 'baidu')
wait.until(EC.frame_to_be_available_and_switch_to_it(locator))

element = driver.find_element_by_id('kw')
print(element)

# driver.switch_to.default_content()
driver.switch_to.parent_frame()