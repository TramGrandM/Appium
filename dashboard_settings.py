from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
#
# from scroll import Scroll
from scroll_and_find import Scroll_and_Find
import time
from test import Test


class Dashboard_setting:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)
        # self.scroll = Scroll(self.driver)
        self.test = Test(self.driver)

    def dashboard_setting(self):
        time.sleep(5)
        setting_btn = self.driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@content-desc="Settings"]')
        setting_btn.click()
        time.sleep(5)
        ele = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/edit_profile_tv" and @text="Dashboard settings"]'
        find_ele = self.scroll_and_find.scroll_and_find(ele)
        # time.sleep(3)
        # print("0000")
        # element = AppiumBy.XPATH, '(//android.widget.Switch[@resource-id="vitalgain.jp:id/dashboard_settings_sw"])'
        # found_element = False
        # while not found_element:
        #     self.scroll.scroll()
        #     find_eles = self.driver.find_elements(*element)
        #     found_element = True
        #     for element in find_eles:
        #         print("Text:", element.text)
        # ele_1 = '(//android.widget.Switch[@resource-id="vitalgain.jp:id/dashboard_settings_sw"])'
        ele_1 = '//androidx.recyclerview.widget.RecyclerView[@resource-id="vitalgain.jp:id/recycler_view"]'
        self.test.scroll_and_find_all(ele_1)
