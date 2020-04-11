from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

# 设置隐式等待及超时时间

driver.implicitly_wait(10)

# 浏览器最大化
driver.maximize_window()


driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")


# 找到拖拽操作的iframe页面

iframe = driver.find_element_by_id("iframeResult")



# 切换到执行拖拽操作的iframe页面
driver.switch_to.frame(iframe)


# 找到拖拽前的元素位置
element_start = driver.find_element_by_id("draggable")



# 找到拖拽的元素目的地
element_end = driver.find_element_by_id("droppable")



# 创建一个鼠标的行动对象
action = ActionChains(driver)



# 执行拖拽操作

action.drag_and_drop(element_start, element_end).perform()
