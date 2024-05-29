import random
import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder


cap: Dict[str, Any] = {
	"platformName": "Android",
	"automationName": "UIAutomator2",
	"deviceName": "emulator-5554",
	"appPackage": "com.mobeta.android.demodslv",
	"appActivity": ".Launcher"
}

url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

wait = WebDriverWait(driver, 10)
el1 = wait.until(EC.presence_of_element_located(("xpath", "//android.widget.Button[@text='Continue']")))
el1.click()

el2 = wait.until(EC.presence_of_element_located(("id", "android:id/button1")))
el2.click()

el3 = wait.until(EC.presence_of_element_located(("xpath", "//android.widget.TextView[@text='Basic usage playground']")))
el3.click()

elements = wait.until(EC.visibility_of_any_elements_located(("xpath", "//android.widget.ImageView["
                                                                   "@resource-id='com.mobeta.android.demodslv:id/drag_handle']" )))
print(len(elements))

actions = ActionChains(driver)
actions.drag_and_drop(elements[random.randint(1,10)], elements[random.randint(1,10)])
actions.perform()
time.sleep(2)
