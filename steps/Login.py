from behave import *
from selenium import webdriver




@given(u'Thực hiện mở trang web')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="chromedriver.exe")
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.driver.get("https://www.saucedemo.com/")


@when(u'Thực hiện nhập username và password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Thực hiện nhập username và password')


@when(u'Thực hiện bấm vào nút Login')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Thực hiện bấm vào nút Login')


@when(u'Thực hiện kiểm tra xem username hiển thị đúng')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Thực hiện kiểm tra xem username hiển thị đúng')


@then(u'thực hiện kiểm tra có hiển thị avatar user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then thực hiện kiểm tra có hiển thị avatar user')
