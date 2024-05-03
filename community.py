import time
from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find


class Community:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def community(self):
        element = AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Glucose")'
        self.scroll_and_find.scroll_and_find(element)