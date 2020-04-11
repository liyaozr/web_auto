import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

driver.get("http://www.baidu.com")

# 元素定位 document.getElementById
# 8 大元素定位方法 8 大金刚 8 大护法
input_elem = driver.find_element_by_id('kw')

# 定位元素得到的是一个 WebElement 对象  DOM
print(input_elem)


# 获取元素以后，可以通过 elem.find_element。。。。 继续查找其中的子元素（嵌套标签）
# print(input_elem.find_element_by_id())

# 获取属性, 获取 ID 属性
# print(input_elem.id)
# 获取文本
print(input_elem.text)
# 通用的获取 name 属性的方式：
print(input_elem.get_attribute('name'))
# 修改属性通过python 修改不了，后面才将：python去发送 js 代码
# input_elem.set_attribute("name", "hello")

# 操作元素, 发送按键。
input_elem.send_keys("柠檬班")

# click(), 点点点
# input_elem.find_element_by_id()
driver.find_element_by_id('su').click()
# 让代码暂停运行
time.sleep(2)
# 2， name



# 3， class_name

# 4, tagname

# 5, link_text,  链接文本

# 6, partial_link_text，   链接文本的一部分

# 7, xpath，

# 8, css_selector

driver.quit()