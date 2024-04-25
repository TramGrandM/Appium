import time
from appium.webdriver.common.appiumby import AppiumBy
from scroll import Scroll
from scroll_and_find import Scroll_and_Find


class Ketone:
    def __init__(self, driver):
        self.driver = driver
        self.scroll = Scroll(self.driver)
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def ketone(self):
        element = AppiumBy.XPATH, '//android.widget.TextView[@text="Ketone"]'
        self.scroll_and_find.scroll_and_find(element)
        add = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="vitalgain.jp:id/add_btn"]')
        add.click()
        actone = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="vitalgain.jp:id/acetone_edt"]')
        actone.send_keys(10)
        input_2 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="vitalgain.jp:id/fat_breakdown_rate_edt"]')
        input_2.send_keys(10)
        add_img = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="vitalgain.jp:id/add_iv"]')
        add_img.click()
        select = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Select photos"]')
        select.click()
        img = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Image"])[1]')
        img.click()
        add_btn = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="vitalgain.jp:id/dialog_add_btn"]')
        add_btn.click()
        time.sleep(3)
        back = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        back.click()
        print("Ketone - Done!")

