import time
from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find


class Water:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def water(self):
        self.driver.implicitly_wait(5)
        element = AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Water")'
        self.scroll_and_find.scroll_and_find(element)
        increase = self.driver.find_element(AppiumBy.XPATH,
                                            '//android.widget.ImageButton[@resource-id="vitalgain.jp:id/water_increase_btn"]')
        increase.click()
        time.sleep(3)
        increase.click()
        decrease = self.driver.find_element(AppiumBy.XPATH,
                                            '//android.widget.ImageButton[@resource-id="vitalgain.jp:id/water_decrease_btn"]')
        decrease.click()
        week = self.driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Weeks"]')
        week.click()
        time.sleep(2)
        month = self.driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@content-desc="Months"]')
        month.click()
        back = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        back.click()
        print("Water - Done!")
