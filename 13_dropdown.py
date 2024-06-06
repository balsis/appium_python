import time
import pytest
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from selenium.common import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap: Dict[str, Any] = {
    "platformName": "Android",
    "automationName": "UIAutomator2",
    "deviceName": "emulator-5554",
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.google.android.apps.contacts.activities.PeopleActivity",
    "enableMultiWindows": True,
    "allowInvisibleElements": False
}

url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

wait = WebDriverWait(driver, 30, poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
wait.until(EC.presence_of_element_located(("xpath", "//android.widget.Button[@text='Allow']"))).click()
wait.until(EC.presence_of_element_located(("accessibility id", "Create contact"))).click()

wait.until(EC.presence_of_element_located(("xpath", "//android.widget.EditText[@text='First name']"))).send_keys("Artur")
wait.until(EC.presence_of_element_located(("xpath", "//android.widget.Spinner[@content-desc='Mobile Phone']"))).click()
wait.until(EC.presence_of_element_located(("xpath", "//android.widget.CheckedTextView[@text='Home Fax']"))).click()
wait.until(EC.presence_of_element_located(("xpath", "//android.widget.EditText[@text='Phone']"))).send_keys("+79111234567")

wait.until(EC.presence_of_element_located(("xpath", "android.widget.Button[@text='Save']"))).click()


time.sleep(3)

driver.quit()