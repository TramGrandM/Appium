import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from scroll import Scroll
from scroll_top import ScrollTop


class Connection:
    def __init__(self, driver):
        self.driver = driver
        self.scroll = Scroll(self.driver)
        self.scroll_top = ScrollTop(self.driver)

    def connection(self):
        time.sleep(3)
        setting_btn = self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Settings"]')
        setting_btn.click()
        choose_hs = self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.TextView[@resource-id="vitalgain.jp:id/edit_profile_tv" and @text="Health data source"]')
        choose_hs.click()
        element = AppiumBy.ID, 'vitalgain.jp:id/register_h_band_device_tv'
        found_element = False
        while not found_element:
            try:
                find_ele = self.driver.find_element(*element)
                found_element = True
                find_ele.click()
            except NoSuchElementException:
                self.scroll.scroll()
        # y4 = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/register_h_band_device_tv')
        # y4.click()
        ok_btn = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/right_button')
        ok_btn.click()
        time.sleep(5)

        # device = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/bluetooth_device_name_tv')
        if self.driver.find_elements(AppiumBy.ID, 'vitalgain.jp:id/bluetooth_device_name_tv'):
            self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/bluetooth_device_name_tv').click()
            ok_btn_1 = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/right_button')
            ok_btn_1.click()
            time.sleep(8)
            back = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
            back.click()
            home = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/item_dashboard')
            home.click()
            self.scroll_top.scroll_top()
            time.sleep(10)
        else:
            print("Not found")
            cancle = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="vitalgain.jp:id/left_button"]')
            cancle.click()
        back = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        back.click()
