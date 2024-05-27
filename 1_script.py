from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions

cap: Dict[str, Any] = {
    "platformName": "Android",
    "automationName": "UIAutomator2",
    "platformVersion": "14",
    "deviceName": "emulator-5554"
}

url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el = driver.find_element("accessibility id", "Chrome")
el.click()
input = driver.find_element("xpath", "//*[@text='Search or type web address']").send_keys('python')
driver.quit()
