"""
============================
Author:luli
Time:2020/3/27
Company:Happy
============================
"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://localhost:63342/web_auto/day5/iframe_demo.html?_ijt=j84c291ib7943970tkfhac160r')

driver.find_element_by_id('btn').click()

wait = WebDriverWait(driver, 30)
wait.until(EC.alert_is_present())

my_alert = driver.switch_to.alert
my_alert.accept()

element = driver.find_element_by_id('p')
print(element)
