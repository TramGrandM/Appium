import time

from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find
from scroll import Scroll


class Grip:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)
        self.scroll = Scroll(self.driver)

    def grip(self):
        element = AppiumBy.XPATH, '//android.widget.TextView[@text="Grip strength"]'
        self.scroll_and_find.scroll_and_find(element)
        add = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/add_btn')
        add.click()
        grip = self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.EditText[@resource-id="vitalgain.jp:id/value_edt"]')
        grip.send_keys(50)
        drop_btn = self.driver.find_element(AppiumBy.XPATH,
                                            '//android.widget.ScrollView[@resource-id="vitalgain.jp:id/layout_content"]/androidx.appcompat.widget.LinearLayoutCompat/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView')
        drop_btn.click()
        left = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Left hand"]')
        left.click()
        add_img = self.driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.ImageView[@resource-id="vitalgain.jp:id/add_iv"]')
        add_img.click()
        select = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Select photos"]')
        select.click()
        img = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Image"])[1]')
        img.click()
        add_btn = self.driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.Button[@resource-id="vitalgain.jp:id/dialog_add_btn"]')
        add_btn.click()
        time.sleep(3)
        back = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        back.click()
        print("Grip strength - Done!")
