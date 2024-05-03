import time
from appium.webdriver.common.appiumby import AppiumBy
from scroll import Scroll
from scroll_and_find import Scroll_and_Find


class Weight:
    def __init__(self, driver):
        self.driver = driver
        self.scroll = Scroll(self.driver)
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def weight(self):
        element = AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="vitalgain.jp:id/dashboard_bmi_view"]'
        self.scroll_and_find.scroll_and_find(element)
        time.sleep(5)
        weight = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="vitalgain.jp:id/dialog_record_weight_edt"]')
        weight.click()
        weight.send_keys('50')
        add_pic = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="vitalgain.jp:id/holder_weight_add_add_iv"]')
        add_pic.click()
        select = self.driver.find_element(AppiumBy.XPATH, '//androidx.appcompat.widget.LinearLayoutCompat[@resource-id="vitalgain.jp:id/photo_selector_gallery_layout"]')
        select.click()
        allow = self.driver.find_element(AppiumBy.XPATH,
                                         '//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_allow_button"]')
        allow.click()
        img = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Image"])[1]')
        img.click()
        add_btn = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="vitalgain.jp:id/dialog_record_weight_add_bt"]')
        add_btn.click()
        time.sleep(8)
        back = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        back.click()
        print("Weight - Done!")
