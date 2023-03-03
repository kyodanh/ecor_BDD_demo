from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains





@when(u'Thực hiên truy cập vào trang cá nhân')
def step_impl(context):
    driver = context.driver
    actions = ActionChains(driver)
    a = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button")
    b = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[1]/a")
    actions.click(a)
    actions.click(b)
    actions.perform()
    time.sleep(2)


@when(u'thực hiện bấm vào change name')
def step_impl(context):
   driver =  context.driver
   action = ActionChains(driver)
   time.sleep(2)
   x = driver.find_element(By.XPATH,"//*[@id='maincontent']/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/a[1]/span")
   action.click(x)
   action.perform()




@when(u'thực hiện nhập tên "panda" mới')
def step_impl(context):
    driver = context.driver
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='firstname']").clear()
    a = driver.find_element(By.XPATH,"//*[@id='firstname']")
    action = ActionChains(driver)
    action.click(a)
    action.send_keys("test123")
    time.sleep(2)
    action.perform()

