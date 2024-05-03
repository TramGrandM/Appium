import time

from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find


class Quit_smoke:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def quit_smoke(self):
        element = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/dashboard_micro_title_tv" and @text="Quit smoking"]'
        self.scroll_and_find.scroll_and_find(element)

        # edit
        edit = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.Button[@text="glossary"])[2]')
        edit.click()
        time.sleep(3)
        edit_ciga = self.driver.find_element(AppiumBy.XPATH,
                                             '//android.app.Dialog/android.view.View[1]/android.view.View/android.widget.EditText')
        edit_ciga.click()
        edit_ciga.clear()
        time.sleep(3)
        self.driver.tap([(100, 950)])
        time.sleep(3)
        self.driver.tap([(270, 1300)])
        cost = self.driver.find_element(AppiumBy.XPATH,
                                        '//android.app.Dialog/android.view.View[2]/android.view.View/android.widget.EditText')
        time.sleep(3)
        cost.click()
        cost.clear()
        self.driver.tap([(270, 950)])
        time.sleep(3)
        self.driver.tap([(270, 1300)])
        time.sleep(3)
        self.driver.tap([(160, 1440)])
        add = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ADD"]')
        add.click()
        # quit_btn = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Quit smoking"]')
        # quit_btn.click()
        time.sleep(3)
        print("Quit smoking - Done! ")
        self.driver.back()
