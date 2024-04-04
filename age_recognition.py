import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from scroll import Scroll


class Age_Recognition:
    def __init__(self, driver):
        self.driver = driver
        self.scroll = Scroll(self.driver)

    def age_recognition(self):
        # device_size = self.driver.get_window_size()
        # print(device_size)
        # width = device_size['width']
        # height = device_size['height']
        # print("width, height", width, "+", height)
        # time.sleep(5)
        #
        # start_x = device_size['width'] / 2
        # start_y = device_size['height'] * 0.3
        # end_x = device_size['width'] / 2
        # end_y = device_size['height'] * 0.7
        # print(start_x, start_y, end_x, end_y)

        # self.driver.swipe(start_y, end_y, start_x, end_x)
        element = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/dashboard_micro_title_tv" and @text="Age Recognition"]'
        found_element = False
        while not found_element:
            try:
                find_ele = self.driver.find_element(*element)
                found_element = True
                find_ele.click()
            except NoSuchElementException:
                self.scroll.scroll()
                # self.driver.swipe(start_y, end_y, start_x, end_x)

    def select_photo(self):
        time.sleep(3)
        camera = self.driver.find_element(AppiumBy.XPATH,
                                          '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]')
        camera.click()

        allow_btn = self.driver.find_element(AppiumBy.XPATH,
                                             '//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_allow_button"]')
        if allow_btn.is_displayed():
            allow_btn.click()
        select_photo = self.driver.find_element(AppiumBy.XPATH,
                                                '//android.widget.LinearLayout[@resource-id="vitalgain.jp:id/register_profile_gallery_layout"]')
        select_photo.click()
        allow_btn_1 = self.driver.find_element(AppiumBy.XPATH,
                                               '//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_allow_button"]')
        if allow_btn_1.is_displayed():
            allow_btn_1.click()

        photos = self.driver.find_element(AppiumBy.XPATH,
                                          '(//android.widget.ImageView[@resource-id="android:id/icon"])[1]')
        photos.click()
        choose_folder = self.driver.find_element(AppiumBy.XPATH,
                                                 '//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]')
        choose_folder.click()
        choose_photo = self.driver.find_element(AppiumBy.XPATH,
                                                '//android.widget.ImageView[@content-desc="Photo taken on Mar 29, 2024 17:01:56"]')
        choose_photo.click()
        choise_btn = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/tv_ok')
        choise_btn.click()
        # self.scroll.scroll()
        time.sleep(3)
        ok_btn = self.driver.find_element(AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[1]/android.widget.Button')
        ok_btn.click()
