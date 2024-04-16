import time

from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find
from scroll import Scroll


class SpO2:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)
        self.scroll = Scroll(self.driver)

    def spo2(self):
        element = AppiumBy.XPATH, '//android.widget.TextView[@text="SpO2"]'
        self.scroll_and_find.scroll_and_find(element)
        add = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="vitalgain.jp:id/add_btn"]')
        add.click()
        spo2 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="vitalgain.jp:id/percent_edt"]')
        spo2.send_keys(98)
        add_img = self.driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.ImageView[@resource-id="vitalgain.jp:id/add_iv"]')
        add_img.click()
        select = self.driver.find_element(AppiumBy.XPATH, '//androidx.appcompat.widget.LinearLayoutCompat[@resource-id="vitalgain.jp:id/photo_selector_gallery_layout"]')
        select.click()
        img = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Image"])[1]')
        img.click()
        add_btn = self.driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.Button[@resource-id="vitalgain.jp:id/dialog_add_btn"]')
        add_btn.click()
        time.sleep(2)
        back = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        back.click()
        print("SpO2 - Done!")
