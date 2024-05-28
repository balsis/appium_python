import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions

cap: Dict[str, Any] = {
    "platformName": "Android",
    "automationName": "UIAutomator2",
    "platformVersion": "13",
    "deviceName": "emulator-5554",
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.google.android.apps.contacts.activities.PeopleActivity"
}

url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(10)

driver.find_element("accessibility id", "Create contact").click()
driver.find_element("xpath", "//android.widget.EditText[@text='First name']").send_keys('Test User')
driver.find_element("xpath", "//android.widget.EditText[@text='Phone']").send_keys('+79111234567')
driver.find_element("xpath", "//android.widget.Button[@text='Save']").click()

time.sleep(4)
driver.quit()
