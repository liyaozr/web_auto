import time
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

# 设置隐式等待的超时时间
# 1， 如果在 30 s 之内找到了元素，那么什么时候找到元素，就什么时候运行下面的代码
# 超过 30s 没有找到，只能报错。不交 NoSuchElement,  TimeOutException.

driver.implicitly_wait(30)

driver.get("https://ke.qq.com")

driver.find_element_by_id("js_login").click()



#查找QQ登录并点击
driver.find_element_by_xpath("//a[@class='js-btns-enter btns-enter btns-enter-qq']").click()


#切换至登录的iframe窗口
wait = WebDriverWait(driver, 30)
wait.until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))
# driver.switch_to.frame("login_frame_qq")



#选择账号密码登录
driver.find_element_by_id("switcher_plogin").click()



#查找QQ号输入框并输入QQ号
driver.find_element_by_id("u").send_keys("3457996284")



#查找密码输入框并输入QQ密码
driver.find_element_by_id("p").send_keys("123")



#查找登录按钮并点击登录
driver.find_element_by_id("login_button").click()




#强制等待5s

time.sleep(5)



#关闭浏览器

driver.quit()
