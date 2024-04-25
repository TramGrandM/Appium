import time
from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find


class Glucose:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def glucose(self):
        element = AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Glucose")'
        self.scroll_and_find.scroll_and_find(element)
        # add record
        time.sleep(3)
        add_record = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Add record"]')
        add_record.click()
        time.sleep(2)
        glu = self.driver.find_element(AppiumBy.XPATH, '//android.app.Dialog/android.view.View/android.view.View[2]/android.view.View')
        glu.click()
        time.sleep(2)
        self.driver.tap([(280, 1050)])
        # self.driver.tap([275, 1300])
        time.sleep(2)
        self.driver.tap([(625, 1065)])
        time.sleep(2)
        self.driver.tap([(160, 1435)])
        time.sleep(5)
        add_img = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="add"]')
        add_img.click()
        allow = self.driver.find_element(AppiumBy.XPATH,
                                         '//android.widget.Button[@resource-id="com.android.packageinstaller:id/permission_allow_button"]')
        allow.click()
        select = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Select photos"]')
        select.click()
        library = self.driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.TextView[@resource-id="android:id/text1" and @text="Gallery"]')
        library.click()
        time.sleep(2)
        img = self.driver.find_element(AppiumBy.XPATH,
                                       '//android.view.View[@resource-id="com.sec.android.gallery3d:id/gl_root_view"]/com.sec.samsung.gallery.glview.composeView.ThumbObject[1]')
        img.click()
        choice = self.driver.find_element(AppiumBy.XPATH,
                                          '//android.widget.TextView[@resource-id="vitalgain.jp:id/tv_ok"]')
        choice.click()
        time.sleep(5)
        save = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="SAVE"]')
        save.click()
        time.sleep(3)
        week = self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@text="Weeks"]')
        week.click()
        time.sleep(2)
        month = self.driver.find_element(AppiumBy.XPATH, '//android.view.View[@text="Months"]')
        month.click()
        time.sleep(2)
        back = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@text="menu"])[1]')
        back.click()
        print("Glucose - Done!")
