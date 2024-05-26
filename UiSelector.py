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
    "platformVersion": "14",
    "deviceName": "emulator-5554",
	"appPackage": "com.google.android.contacts",
	"appActivity": "com.google.android.apps.contacts.activities.PeopleActivity"
}

url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
# driver.implicitly_wait(50)

wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
el = wait.until(EC.presence_of_element_located(("xpath", "//android.widget.Button[@text='Skip']")))
el.click()

wait.until(EC.presence_of_element_located(("accessibility id", "Create contact"))).click()
driver.find_element("-android uiautomator", "new UiSelector().text(\"First name\")").send_keys('Test User')
# driver.find_element("xpath", "//android.widget.EditText[@text='First name']").send_keys('Test User')
driver.find_element("xpath", "//android.widget.EditText[@text='Phone']").send_keys('+79111234567')
driver.find_element("xpath", "//android.widget.Button[@text='Save']").click()

time.sleep(4)
driver.quit()
