from selenium import webdriver

# 启动浏览器 Chrome 是大写的。
browser = webdriver.Chrome(executable_path=r'D:\\chromedriver.exe')

# 打开 url 地址
browser.get('http://www.baidu.com')

# 其他的操作。。。。

# 关闭浏览器
browser.quit()
