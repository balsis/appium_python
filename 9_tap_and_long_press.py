import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

cap: Dict[str, Any] = {
    "platformName": "Android",
    "automationName": "UIAutomator2",
    "platformVersion": "13",
    "deviceName": "emulator-5554",
    "appPackage": "com.google.android.contacts",
    "appActivity": "com.google.android.apps.contacts.activities.PeopleActivity"
}

url = 'http://127.0.0.1:4723'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

wait = WebDriverWait(driver, 20)
el0 = wait.until(EC.presence_of_element_located(("id", "android:id/button2")))
if el0.is_displayed():
    el0.click()
    el1 = wait.until(
        EC.presence_of_element_located(("id", "com.android.permissioncontroller:id/permission_allow_button")))
    el1.click()

el2 = wait.until(EC.presence_of_element_located(("id",
                                                 "test")))
el2.click()
# coord = list(el2.values())
# print(coord)
# actions = ActionChains(driver)
# actions.click_and_hold(el2)
# actions.w3c_actions.pointer_action.pointer_down(x=coord[0], y=coord[1]).perform()
