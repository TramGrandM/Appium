import time
from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find


class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def logout(self):
        setting = self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Settings"]')
        setting.click()
        element = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/edit_profile_tv" and @text="Logout"]'
        self.scroll_and_find.scroll_and_find(element)
        ok_btn = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="vitalgain.jp:id/right_button"]')
        ok_btn.click()
        