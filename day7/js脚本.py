"""
============================
Author:luli
Time:2020/3/30
Company:Happy
============================
"""
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.12306.cn/index/')
driver.implicitly_wait(30)

# 尝试1：这种方法不生效，因为定位元素需要时间，而我们无法让它在中间等待2秒
# js_code = '''
# train_date = document.getElementById('train_date');
# train_date.readOnly = false;
# train_date.value = '2021-06-22';
# '''
# driver.execute_script(js_code)

# 尝试2：日期选择这个元素，使用常规的selenium方法无法选择
# train_date = driver.find_element_by_id('train_date')
# js_code = 'arguments[0].readOnly = false'
# driver.execute_script(js_code, train_date)
#
# time_str = '2020-06-12'
# js_code = 'arguments[0].value = "{}"'.format(time_str)
# driver.execute_script(js_code, train_date)

# 尝试3：下面这种写法，中间不加time.sleep也不行
train_date = driver.find_element_by_id('train_date')
print(train_date)
time.sleep(2)
js_code = 'arguments[0].readOnly = false;arguments[0].value = "2020-06-12";'
driver.execute_script(js_code, train_date)

time.sleep(5)
driver.quit()
