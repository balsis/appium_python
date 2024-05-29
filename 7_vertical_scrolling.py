import time
from appium import webdriver
from typing import Any, Dict
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


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
el1 = wait.until(EC.presence_of_element_located(("xpath", "//android.widget.TextView[@text='App']")))
el1.click()

el2 = wait.until(EC.presence_of_element_located(("xpath", "//android.widget.TextView[@text='Activity']")))
el2.click()



# uiautomator scroll to end
el3 = driver.find_element('-android uiautomator', 'new UiScrollable(new UiSelector().scrollable('
                                                  'true)).setAsVerticalList().scrollToEnd(5, 3)')

# uiautomator scroll to start

el4 = driver.find_element('-android uiautomator', 'new UiScrollable(new UiSelector().scrollable('
                                                  'true)).setAsVerticalList().scrollToBeginning(5, 3)')
## ActionsChains scroll

# device_size = driver.get_window_size()
# print(device_size)
# screen_width = device_size['width']
# screen_height = device_size['height']
# print(screen_width, screen_height)
#
# start_x = screen_width / 2
# end_x = screen_width / 2
# start_y = screen_height * 8 / 9
# end_y = screen_height / 3
#
# actions = ActionChains(driver)
# actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
# time.sleep(2)
#
# actions = ActionChains(driver)
# actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
# actions.w3c_actions.pointer_action.pointer_down()
# actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
# actions.w3c_actions.pointer_action.release()
# actions.perform()
# time.sleep(2)
# driver.swipe(100, 3000, 100, 100)


driver.quit()
