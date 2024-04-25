import random
import time
from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find


class Change_avt:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def Change_avt(self):
        edit = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/avatar_iv')
        edit.click()
        edit_avt = self.driver.find_element(AppiumBy.XPATH, 'vitalgain.jp:id/edit_profile_avatar')
        edit_avt.click()
        select = self.driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vitalgain.jp:id/register_profile_gallery_layout"]')
        select.click()
        gallery = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="Gallery"]')
        gallery.click()
        img = self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="com.sec.android.gallery3d:id/gl_root_view"]/com.sec.samsung.gallery.glview.composeView.ThumbObject[1]')
        img.click()
