"""测试登录功能。

流程：
1，启动浏览器，打开url;
2, 定位用户名；
3， 输入用户名；
4， 定位密码；
5， 输入密码；
6， 定位登录按钮；
7， 点击登录按钮；
8，定位错误信息断言
"""
import time
import unittest
import ddt
from selenium import webdriver
from selenium.webdriver.common.by import By

from web_09_web自动化测试项目_v2.data import login_data_error, login_data_invalid, login_data_success
from web_09_web自动化测试项目_v2.pages.home_page import HomePage
from web_09_web自动化测试项目_v2.pages.login_page import LoginPage


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        # 设置隐式等待
        wait_timeout = 20
        self.driver.implicitly_wait(wait_timeout)

    def tearDown(self) -> None:
        self.driver.quit()

    # @ddt.data(*login_data_error)
    # def test_login_username_empty(self, test_info):
    #     # 第一步：获取预期结果
    #     expected = test_info['expected']
    #     # 第二部：获取实际结果（调用页面行为的方法）
    #     LoginPage(self.driver).login(test_info["mobile"], test_info["pwd"])
    #
    #     error_msg = LoginPage(self.driver).get_error_msg()
    #     # 第三部：断言
    #     try:
    #         self.assertEqual(error_msg, expected)
    #         # 记录日志，截取错误截图。
    #     except AssertionError as e:
    #         print("测试用例没有通过")
    #         # 测试用例的断言还生效吗？？断言失败抛出异常。
    #         raise e

    # @ddt.data(*login_data_invalid)
    # def test_login_invalid_user(self, test_info):
    #     expected = test_info['expected']
    #     LoginPage(self.driver).login(test_info["mobile"], test_info["pwd"])
    #     invalid_msg = LoginPage(self.driver).get_invalid_msg()
    #     try:
    #         self.assertEqual(invalid_msg, expected)
    #     except AssertionError as e:
    #         raise e

    @ddt.data(*login_data_success)
    def test_login_success_user(self, test_info):
        expected = test_info['expected']
        LoginPage(self.driver).login(test_info["mobile"], test_info["pwd"])

        # 跳转到首页。
        # 定位首页的元素
        # 隐式等待能不能等待新页面出现
        # 显示等待， 强制等待，等待新页面出现
        # titleCotains, url_contains
        time.sleep(0.3)

        account_msg = HomePage(self.driver).get_user_info()
        try:
            self.assertEqual(account_msg, expected)
        except AssertionError as e:
            raise e
