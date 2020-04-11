from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

driver.get("http://www.baidu.com")

# 元素定位
# e 是什么类型？？WebElement 对象
e = driver.find_element_by_id('kw')

# es 是什么数据类型？？ 列表
es = driver.find_elements_by_id("kw")
print(es)

# 第一条规律： 通过ID 定位只能找到一个元素，不会是多个。
# 原因：一个HTML的文档ID 是唯一的。不存在 2 个元素的 ID 相等
# 只有 ID 是唯一的
# 到底唯一好，还是不唯一好。
# 能用 ID 定位就用 ID 定位
# ID 是有坑的。 有 ID 属性的元素比较少。
# ID 可以是动态变化的。
# 当 ID 你觉得有可能发生变化，就不要使用 ID 定位了。
# 套路1， id=有数字 123 可能是发生变化的
# 套路2， id=ofwofmcwefjoewlmclwc     su, su_1

#  name=123, name = owofmoc

# name, class_name
# driver.find_element_by_name("wd")
# driver.find_elements_by_name("wd")

# class_name

#find_element 比雨泽还懒，只要他找到了符合要求的元素，直接返回，后面的不管了。
# e = driver.find_element_by_class_name("mnav") #
# elements = driver.find_elements_by_class_name("mnav")
# print(len(elements))
# print(e.text)

# 定位元素（确保元素定位方式的唯一性，精准）
# 方法1， 在浏览器当中使用搜索
# 方法2， python 当中find_elements_.... 打印，如果出现多个，

# class_name 的第二个坑： 元素定位当中不能有空格。
#
e = driver.find_element_by_class_name('sp')
print(e.text)

# ID, name, class_name 虽然说有坑，但是这 3个是用得最多的元素定位方式。

# 不想用，通过标签名 tagname
e = driver.find_element_by_tag_name("a")

# link_text 唯一性比较强，只能定位链接， a
# 新闻
# partial_text_text 也是。   一部分
driver.find_element_by_partial_link_text('闻')

# 一把手，生产环境，vim
# xpath
# css