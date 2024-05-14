from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions

cap: Dict[str, Any] = {
    "platformName": "Android",
    "automationName": "UIAutomator2",
    "platformVersion": "13",
    "deviceName": "emulator-5554",
    "appPackage": "com.android.settings",
    "appActivity": ".Settings",
    "language": "en",
    "locale": "US"
}

url = 'http://192.168.1.9:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el = driver.find_element("xpath", "//*[@text='Battery']")
el.click()
driver.quit()
