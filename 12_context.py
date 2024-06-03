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
	"deviceName": "emulator-5554",
	"appPackage": "com.socialnmobile.dictapps.notepad.color.note",
	"appActivity": "com.socialnmobile.colornote.activity.Main",
	# "autoWebview": "true"
}

url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

wait = WebDriverWait(driver, 30, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
wait.until(EC.presence_of_element_located(("xpath", "//android.widget.Button[@text='NEXT']"))).click()
wait.until(EC.presence_of_element_located(("xpath", "//android.widget.Button[@text='NEXT']"))).click()
wait.until(EC.presence_of_element_located(("xpath", "//android.widget.Button[@text='Allow']"))).click()
wait.until(EC.presence_of_element_located(("xpath", "//android.widget.Button[@text='SKIP']"))).click()
wait.until(EC.presence_of_element_located(("-android uiautomator", "new UiSelector().resourceId(\"com.socialnmobile.dictapps.notepad.color.note:id/icon\").instance(4)"))).click()
wait.until(EC.presence_of_element_located(("xpath", "//android.widget.TextView[@text='Like us on Facebook']"))).click()
print(driver.current_context)
print(driver.contexts)
time.sleep(5)
print(driver.current_context)
print(driver.contexts)
# wait.until(EC.presence_of_element_located(("xpath", "//android.widget.Button[@text='󱤅']"))).click()
# wait.until(EC.presence_of_element_located(("xpath", "//android.widget.TextView[@text='About']"))).click()
driver.switch_to.context(driver.contexts[1])
print(driver.current_context)
print(driver.contexts)
driver.quit()


