from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains





@when(u'Thực hiên truy cập vào trang cá nhân')
def step_impl(context):
    driver = context.driver
    actions = ActionChains(driver)
    a = driver.find_element(By.XPATH,"//button[@type='button']")
    b = driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
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


@when(u'thực hiện nhập tên "{user_fristname}" và "{user_lastname}" mới')
def step_impl(context,user_fristname,user_lastname):
        driver = context.driver
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='firstname']").clear()
        driver.find_element(By.XPATH, "//*[@id='lastname']").clear()
        a = driver.find_element(By.XPATH, "//*[@id='firstname']")
        b = driver.find_element(By.XPATH, "//*[@id='lastname']")
        action = ActionChains(driver)
        action.click(a)
        action.send_keys(user_fristname)
        time.sleep(2)
        action.perform()
        action.click(b)
        action.send_keys(user_lastname)
        time.sleep(2)
        action.perform()


@then(u'thực hiện kiểm tra tên đã thay đổi')
def step_impl(context):
    driver = context.driver
    action = ActionChains(driver)
    a = driver.find_element(By.XPATH,"//*[@id='form-validate']/div/div[1]/button")
    action.click(a)
    action.perform()
    time.sleep(3)
    a = driver.find_element(By.XPATH,"//*[@id='maincontent']/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/p").text
    print("thông tin đã được thay đổi thành " + a)
    time.sleep(2)






