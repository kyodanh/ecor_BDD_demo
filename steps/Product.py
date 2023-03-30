from behave import *
from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains




@when(u'Thực hiện chuyển tới trang cuối của màn hình')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


@when(u'Kiểm tra 1 sản phẩm bất kì có trên trang')
def step_impl(context):
    time.sleep(3)
    driver = context.driver
    actions = ActionChains(driver)
    # lấy màu xanh
    color_blue = driver.find_element(By.XPATH,("//*[@id='option-label-color-93-item-50']"))
    actions.click(color_blue)
    actions.perform()
    time.sleep(10)
    print(driver.find_element(By.XPATH,("//*[@id='maincontent']/div[3]/div/div[2]/div[3]/div/div/ol/li[1]/div/a/span/span/img")).get_attribute("src"))
    # lấy màu cam
    color_organe = driver.find_element(By.XPATH,("//*[@id='option-label-color-93-item-56']"))
    actions.click(color_organe)
    actions.perform()
    time.sleep(10)
    print(driver.find_element(By.XPATH,("//*[@id='maincontent']/div[3]/div/div[2]/div[3]/div/div/ol/li[1]/div/a/span/span/img")).get_attribute("src"))
    # lấy màu tím
    color_organe = driver.find_element(By.XPATH, ("//*[@id='option-label-color-93-item-57']"))
    actions.click(color_organe)
    actions.perform()
    time.sleep(10)
    print(driver.find_element(By.XPATH, ("//*[@id='maincontent']/div[3]/div/div[2]/div[3]/div/div/ol/li[1]/div/a/span/span/img")).get_attribute("src"))




# @then(u'thực hiện kiểm tra màu sản phẩm')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then thực hiện kiểm tra màu sản phẩm')


@then(u'thực hiện kiểm tra màu "{color}" "{mau}" "{maucancheck}"sản phẩm')
def step_impl(context,color,mau,maucancheck):
    time.sleep(3)
    driver = context.driver
    actions = ActionChains(driver)
    color_x = driver.find_element(By.XPATH, (color))
    actions.click(color_x)
    actions.perform()
    time.sleep(10)
    src = driver.find_element(By.XPATH, ("//*[@id='maincontent']/div[3]/div/div[2]/div[3]/div/div/ol/li[1]/div/a/span/span/img")).get_attribute("src")
    if src == (mau) :
        print("màu áo đang là màu " + maucancheck)
    else:
        print("không phải màu xanh")



@when(u'Thực hiện chuyển lên đầu trang')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.TAG_NAME, ("html")).send_keys(Keys.HOME)
    time.sleep(3)

@when(u'Thực hiện tại bấm vào banner yoga đầu trang')
def step_impl(context):
    time.sleep(3)
    diver = context.driver
    diver.find_element(By.XPATH,("//*[@id='maincontent']/div[3]/div/div[2]/div[1]/a/span/span[2]")).click()


@then(u'Hệ thống chuyển qua trang yoga và hệ thống hiển thị sản phẩm')
def step_impl(context):
    time.sleep(3)
    diver = context.driver
    a = diver.find_element(By.XPATH,("//*[@id='page-title-heading']/span")).text
    if a == ("New Luma Yoga Collection"):
        print("hệ thống đã chuyển qua trang " + a)
    else:
        print("Sai")
    time.sleep(3)
    diver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)


# @when(u'Bấm vào 1 sản phẩm "(product)" trên trang để xem chi tiết')
# def step_impl(context,product):
#     time.sleep(3)
#     diver = context.driver
#     diver.find_element(By.XPATH,(product)).click()
#     time.sleep(3)


@when(u'Bấm vào 1 sản phẩm "{product}" trên trang để xem chi tiết')
def step_impl(context,product):
    time.sleep(3)
    diver = context.driver
    diver.find_element(By.LINK_TEXT, (product)).click()
    time.sleep(3)

# @when(u'bấm vào sản phẩm')
# def step_impl(context):
#     time.sleep(3)
#     diver = context.driver
#     diver.find_element(By.LINK_TEXT, ("Echo Fit Compression Short")).click()
#     time.sleep(3)

@then(u'Hệ thống hiển thị thông tin chi tiết cho sản phẩm')
def step_impl(context):
    time.sleep(3)
