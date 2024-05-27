import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

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
	wait = WebDriverWait(driver, 20)
	el = wait.until(EC.presence_of_element_located(("id", "android:id/button1")))
	el.click()

wait = WebDriverWait(driver, 10, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
el1 = wait.until(EC.presence_of_element_located(("xpath", "//android.widget.TextView[@text='Views']")))
el1.click()

el2 = wait.until(EC.presence_of_element_located(("xpath", "//android.widget.TextView[@text='Gallery']")))
el2.click()

el3 = wait.until(EC.presence_of_element_located(("xpath", "//android.widget.TextView[@text='1. Photos']")))
el3.click()

##########
# driver.find_element('-android uiautomator', 'new UiScrollable(new UiSelector().scrollable('
#                                             'true)).setAsHorizontalList().scrollToEnd(5)')
# driver.find_element('-android uiautomator', 'new UiScrollable(new UiSelector().scrollable('
#                                             'true)).setAsHorizontalList().scrollToBeginning(5)')

driver.find_element('-android uiautomator', 'new UiScrollable(new UiSelector().scrollable('
                                            'true)).setAsHorizontalList().scrollForward(5)')

####