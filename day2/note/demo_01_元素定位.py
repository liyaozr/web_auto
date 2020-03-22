
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# 元素定位 document.getElementById
# 8 大元素定位方法 8 大金刚 8 大护法
id = driver.find_element_by_id('kw')
print(id)

# 2， name

# 3， class_name

# 4, tagname

# 5, link_text,  链接文本

# 6, partial_link_text，   链接文本的一部分

# 7, xpath，

# 8, css_selector

driver.quit()