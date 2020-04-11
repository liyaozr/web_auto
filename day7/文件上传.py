"""
============================
Author:luli
Time:2020/4/2
Company:Happy
============================
"""
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(30)

driver.find_element_by_class_name('soutu-btn').click()

file_btn = driver.find_element_by_class_name('upload-pic')
# 方法1：直接使用send_keys
# file_btn.send_keys(r'E:\test.jpg')

# 方法2：pyautogui

import pyperclip
import pyautogui as ui

# 如果文件是中文名称，先使用pyperclip复制一下，如果是英文省略这个步骤
# 中文路径
# file_btn.click()
# pyperclip.copy(r'E:\test.jpg')
# time.sleep(2)
# ui.hotkey('ctrl', 'v')
# time.sleep(2)
# ui.press('enter', presses=2)
# 英文路径
# ui.write(r'E:\test.jpg')
# time.sleep(2)
# ui.press('enter', presses=2)

# 方法3：pywinauto
from pywinauto import Desktop

file_btn.click()
time.sleep(2)
app = Desktop()
dialog = app['打开']  # 根据名字找到窗口
dialog['Edit'].type_keys(r'E:\test.jpg')
dialog['button'].click()
# from pywinauto import application
# file_btn.click()
# time.sleep(2)  # 需要稍作等待，因为点击上传按钮到文件选择窗口打开会有延迟
# app = application.Application()  # 实例化Application
# 这里用的class而没有加窗口title，主要为了保证兼容性
# app.connect(class_name='#32770')  # 根据class_name找到弹出窗口
# app["Dialog"]["Edit1"].type_keys(r'E:\test.jpg')  # 在输入框中输入值
# app["Dialog"]["Button1"].click()

time.sleep(5)
driver.quit()
