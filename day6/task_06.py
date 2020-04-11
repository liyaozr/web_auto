"""
============================
Author:luli
Time:2020/3/29
Company:Happy
============================
"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.maximize_window()
driver.implicitly_wait(30)

# driver.find_element_by_id('submitBTN').click()
# 切换iframe
wait = WebDriverWait(driver, 30)
locator = ('id', 'iframeResult')
wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
# 定位拖动元素和目标元素
drag = driver.find_element_by_id('draggable')
drop = driver.find_element_by_id('droppable')
# 拖拽
action = ActionChains(driver)
action.drag_and_drop(drag, drop)
action.perform()

time.sleep(3)
driver.quit()
