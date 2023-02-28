import time

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import get_remote_connection


@given(u'Thực hiện mở trang web')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="chromedriver.exe")
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.driver.get("https://magento.softwaretestingboard.com/")


@when(u'Thực hiện nhập "{username}" và "{password}"')
def step_impl(context,username,password):
    driver = context.driver
    driver.find_element(By.XPATH,"//li[2]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='email']").send_keys(username)
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='pass']").send_keys(password)
    time.sleep(2)




@when(u'Thực hiện bấm vào nút Login')
def step_impl(context):
    driver = context.driver
    driver.find_element(By.XPATH,"//*[@id='send2']/span").click()

@when(u'Thực hiện kiểm tra xem username hiển thị đúng')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Thực hiện kiểm tra xem username hiển thị đúng')


@then(u'thực hiện kiểm tra có hiển thị avatar user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then thực hiện kiểm tra có hiển thị avatar user')
