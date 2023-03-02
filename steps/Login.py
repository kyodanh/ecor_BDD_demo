from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@given(u'Thực hiện mở trang web')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="chromedriver.exe")
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.driver.get("https://magento.softwaretestingboard.com/")


@when(u'Thực hiện nhập "{username}" và "{password}"')
def step_impl(context,username,password):
    driver = context.driver
    actions = ActionChains(driver)
    a = driver.find_element(By.XPATH, "//li[2]/a")
    actions.click(a)
    actions.perform()
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='email']").send_keys(username)
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id='pass']").send_keys(password)
    time.sleep(2)




@when(u'Thực hiện bấm vào nút Login')
def step_impl(context):
    # context.driver
    # action = ActionChains(context.driver)
    # x = context.driver.find_element(By.XPATH,"//*[@id='send2']")
    # action.click(x)
    context.driver.find_element(By.XPATH,"//*[@id='send2']").click()
@when(u'Thực hiện kiểm tra xem username hiển thị đúng')
def step_impl(context):
   time.sleep(2)
   # print(context.driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[1]/span").text)
   driver = context.driver
   x = driver.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[1]/span").text
   print(x)
   if x == ("Welcome, danh nguyen!"):
       print(x + " user hiển thị đúng và đăng nhập đúng thông tin ")
   else:
       print(x + "user hiển thị sai và đăng nhập sai thông tin")
   time.sleep(2)

@then(u'thực hiện kiểm tra có hiển thị avatar user')
def step_impl(context):
    driver = context.driver
    # context.driver.find_element(By.XPATH,"").click()
    time.sleep(2)

# ////////////////////////
@when(u'Thực hiện bấm vào trang cá nhân của user')
def step_impl(context):
    driver = context.driver
    actions = ActionChains(driver)
    a = driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button")
    b = driver.find_element(By.XPATH,"/html/body/div[2]/header/div[1]/div/ul/li[2]/div/ul/li[1]/a")
    actions.click(a)
    actions.click(b)
    actions.perform()
    time.sleep(2)





@then(u'thực hiện kiểm tra thông tin user có giống với menu')
def step_impl(context):
    driver = context.driver
    a = driver.find_element(By.XPATH, "//*[@id='maincontent']/div[2]/div[1]/div[3]/div[2]/div[1]/strong").text
    b = driver.find_element(By.XPATH, "//*[@id='maincontent']/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/p").text
    print(a)
    print(b)
    time.sleep(3)