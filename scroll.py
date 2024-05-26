import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy


cap: Dict[str, Any] = {
    "platformName": "Android",
    "automationName": "UIAutomator2",
    "platformVersion": "13",
    "deviceName": "emulator-5554",
	"appPackage": "com.hmh.api",
	"appActivity": ".ApiDemos"
}

url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
if driver.find_element("xpath", "//android.widget.Button[@text='Continue']").is_displayed():
	driver.find_element("xpath", "//android.widget.Button[@text='Continue']").click()
	wait = WebDriverWait(driver, 10)
	el = wait.until(EC.presence_of_element_located(("id", "android:id/button1")))
	el.click()

wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
el1 = wait.until(EC.presence_of_element_located(("xpath", "//android.widget.TextView[@text='App']")))
el1.click()

el2 = wait.until(EC.presence_of_element_located(("xpath", "//android.widget.TextView[@text='Activity']")))
el2.click()

el3 = driver.find_element('-android uiautomator', 'new UiScrollable(new UiSelector().scrollable('
                                                  'true)).scrollIntoView(new UiSelector().text("Wallpaper"))')
el3.click()
# wait.until(EC.presence_of_element_located(("accessibility id", "Create contact"))).click()
# driver.find_element("-android uiautomator", "new UiSelector().text(\"First name\")").send_keys('Test User')
# # driver.find_element("xpath", "//android.widget.EditText[@text='First name']").send_keys('Test User')
# driver.find_element("xpath", "//android.widget.EditText[@text='Phone']").send_keys('+79111234567')
# driver.find_element("xpath", "//android.widget.Button[@text='Save']").click()
#
# time.sleep(4)
driver.quit()
