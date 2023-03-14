from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains




@when(u'Thực hiện chuyển tới trang cuối của màn hình')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


@when(u'Kiểm tra 1 sản phẩm bất kì có trên trang')
def step_impl(context):
    time.sleep(3)


@then(u'thực hiện kiểm tra màu sản phẩm')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then thực hiện kiểm tra màu sản phẩm')
