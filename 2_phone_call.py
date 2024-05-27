import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions

cap: Dict[str, Any] = {
    "platformName": "Android",
    "automationName": "UIAutomator2",
    "platformVersion": "14",
    "deviceName": "emulator-5554",
	"appPackage": "com.google.android.dialer",
	"appActivity": "com.android.dialer.main.impl.MainActivity"
}

url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))


driver.find_element("xpath", "//android.widget.TextView[@text='Recents']").click()
driver.find_element("accessibility id", "key pad").click()

driver.find_element("xpath", "//android.widget.TextView[@text='7']").click()
driver.find_element("xpath", "//android.widget.TextView[@text='9']").click()
driver.find_element("xpath", "//android.widget.TextView[@text='1']").click()
driver.find_element("xpath", "//android.widget.TextView[@text='1']").click()
driver.find_element("xpath", "//android.widget.TextView[@text='9']").click()
driver.find_element("xpath", "//android.widget.TextView[@text='9']").click()

driver.find_element("accessibility id", "dial").click()

time.sleep(4)
driver.quit()
