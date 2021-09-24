import behave_webdriver
from selenium.webdriver.support.ui import WebDriverWait


def before_all(context):
    context.driver = behave_webdriver.Chrome()
    context.wait = WebDriverWait(context.driver, 10)


def after_all(context):
    context.driver.quit()
