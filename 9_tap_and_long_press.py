import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

cap: Dict[str, Any] = {
	"platformName": "Android",
	"automationName": "UIAutomator2",
	"deviceName": "emulator-5554",
	"clearSystemFiles": "true",
	"appPackage": "com.google.android.contacts",
	"appActivity": "com.google.android.apps.contacts.activities.PeopleActivity"
}

appium_server = AppiumService()
appium_server.start()
# url = 'http://127.0.0.1:4723'
driver = webdriver.Remote('http://0.0.0.0:4723', options=AppiumOptions().load_capabilities(cap))

wait = WebDriverWait(driver, 10)
el0 = wait.until(EC.presence_of_element_located(("id", "android:id/button2")))
if el0.is_displayed():
	el0.click()
# el1 = wait.until(EC.presence_of_element_located(("id", "com.android.permissioncontroller:id/permission_allow_button")))
# if el1.is_displayed():
#     el1.click()

el2 = wait.until(EC.presence_of_element_located(("xpath",
                                                 "//android.widget.TextView[@content-desc='Test']")))
el2_coord = [tuple(el2.location.values())]

## tap
# driver.tap(el2_coord, 50)
# time.sleep(3)

## long press
actions = ActionChains(driver)
actions.click_and_hold(el2)
actions.pause(1)
actions.perform()
time.sleep(2)
appium_server.stop()



