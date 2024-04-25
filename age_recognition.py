import time
from appium.webdriver.common.appiumby import AppiumBy
from scroll import Scroll
from scroll_and_find import Scroll_and_Find


class Age_Recognition:
    def __init__(self, driver):
        self.driver = driver
        self.scroll = Scroll(self.driver)
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def age_recognition(self):
        # element = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/dashboard_micro_title_tv" and @text="見た目分析AI"]'
        element = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/dashboard_micro_title_tv" and @text="Age Recognition"]'
        # element = AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="vitalgain.jp:id/main_dashboard_flex_layout"]/android.widget.FrameLayout[4]/android.view.ViewGroup'
        # found_element = False
        # while not found_element:
        #     try:
        #         find_ele = self.driver.find_element(*element)
        #         found_element = True
        #         find_ele.click()
        #     except NoSuchElementException:
        #         self.scroll.scroll()
        self.scroll_and_find.scroll_and_find(element)

    def select_photo(self):
        time.sleep(3)
        camera = self.driver.find_element(AppiumBy.XPATH,
                                          '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]')
        camera.click()
        # if self.driver.find_element(AppiumBy.XPATH,
        #                             '//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_allow_button"]').is_displayed():
        #     self.driver.find_element(AppiumBy.XPATH,
        #                              '//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_allow_button"]').click()
        select_photo = self.driver.find_element(AppiumBy.XPATH,
                                                '//android.widget.LinearLayout[@resource-id="vitalgain.jp:id/register_profile_gallery_layout"]/android.widget.TextView')
        # assert select_photo.text == '写真を選択'
        select_photo.click()
        # if self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_allow_button"]').is_displayed():
        #     self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_allow_button"]').click()

        # photos = self.driver.find_element(AppiumBy.XPATH,
        #                                   '(//android.widget.ImageView[@resource-id="android:id/icon"])[2]')
        # photos.click()
        choose_folder = self.driver.find_element(AppiumBy.XPATH,
                                                 '//android.widget.TextView[@resource-id="android:id/text1" and @text="Gallery"]')
        choose_folder.click()
        time.sleep(3)
        choose_photo = self.driver.find_element(AppiumBy.XPATH,
                                                '//android.view.View[@resource-id="com.sec.android.gallery3d:id/gl_root_view"]/com.sec.samsung.gallery.glview.composeView.ThumbObject[1]')
        choose_photo.click()
        choise_btn = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/tv_ok')
        choise_btn.click()
        # self.scroll.scroll()
        time.sleep(5)
        ok_btn = self.driver.find_element(AppiumBy.XPATH,
                                          '//android.app.Dialog/android.view.View/android.view.View[1]/android.widget.Button')
        ok_btn.click()

    def take_a_picture(self):
        time.sleep(3)
        # text = self.driver.find_element(AppiumBy.XPATH,
        #                                 '//android.widget.TextView[@text="カメラで撮影して\n診断開始"]')
        # print("Text:", text.text)
        # assert text.text == "カメラで撮影して\n診断開始"
        camera = self.driver.find_element(AppiumBy.XPATH,
                                          '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[2]/android.view.View[1]')
        camera.click()

        # allow_btn = self.driver.find_element(AppiumBy.XPATH,
        #                                      '//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_allow_button"]')
        # if allow_btn.is_displayed():
        #     allow_btn.click()
        time.sleep(5)
        take_apicture = self.driver.find_element(AppiumBy.XPATH,
                                                 '//android.widget.LinearLayout[@resource-id="vitalgain.jp:id/register_profile_camera_layout"]/android.widget.TextView')
        # assert take_apicture.text == '写真を撮る'
        take_apicture.click()

        # time.sleep(5)
        # allow_btn_1 = self.driver.find_element(AppiumBy.XPATH,
        #                                        '//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_allow_button"]')
        # time.sleep(5)
        # if allow_btn_1.is_displayed():
        #     allow_btn_1.click()
        # time.sleep(5)
        take_btn = self.driver.find_element(AppiumBy.XPATH, '//GLButton[@content-desc="NONE" and @text="Shutter"]')
        # take_btn = self.driver.find_element(AppiumBy.XPATH, '(//GLViewGroup[@content-desc="NONE"])[6]/GLButton[2]')
        take_btn.click()
        time.sleep(5)
        btn_ok = self.driver.find_element(AppiumBy.ID, 'com.sec.android.app.camera:id/okay')
        btn_ok.click()
        btn_use = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/tv_ok')
        btn_use.click()
        time.sleep(5)
        # text_2 = self.driver.find_element(AppiumBy.XPATH,
        #                                   '//android.widget.TextView[@text="写真で人の顔が写っていることが検出できません。"]')
        # assert text_2.text == '写真で人の顔が写っていることが検出できません。'
        # print("Text 2 :", text_2.text)
        btn_ok_1 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="OK"]')
        btn_ok_1.click()
        print("Age Recognition - Done!")
