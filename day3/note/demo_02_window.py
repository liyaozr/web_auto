from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"d:\chromedriver.exe")

driver.get("http://www.baidu.com")

# 最大化
driver.maximize_window()

# 最小化
driver.minimize_window()

# 设置窗口大小
driver.set_window_size(800, 600)

# 刷新
driver.refresh()

# 打开新页面
driver.get("http://www.douban.com")

# 后退
driver.back()

# 前进
driver.forward()

# 获取 title
print(driver.title) # 豆瓣

print(driver.current_url) # douban.com

print(driver.page_source)

print(driver.window_handles) #2

# close 关闭标签页（窗口）
driver.close()
# quit 关闭整个浏览器
driver.quit()