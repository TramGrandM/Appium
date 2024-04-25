import time

from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find


class Change_avt:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def change_avt(self):
        time.sleep(5)
        edit = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/avatar_iv')
        edit.click()
        time.sleep(5)
        edit_avt = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="vitalgain.jp:id/edit_profile_avatar"]')
        edit_avt.click()
        # select photo
        select = self.driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="vitalgain.jp:id/register_profile_gallery_layout"]')
        select.click()
        gallery = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1" and @text="Gallery"]')
        gallery.click()
        img = self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="com.sec.android.gallery3d:id/gl_root_view"]/com.sec.samsung.gallery.glview.composeView.ThumbObject[1]')
        img.click()
        choice = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/tv_ok"]')
        choice.click()
        # take photo
        time.sleep(10)
        edit_avt.click()
        take = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Take a picture"]')
        take.click()
        shutter = self.driver.find_element(AppiumBy.XPATH, '//GLButton[@content-desc="NONE" and @text="Shutter"]')
        shutter.click()
        time.sleep(3)
        ok_btn = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.sec.android.app.camera:id/okay"]')
        ok_btn.click()
        use_photo = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/tv_ok"]')
        use_photo.click()
        print("Change avt - Done!")


