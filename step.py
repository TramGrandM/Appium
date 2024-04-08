import time

from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find


class Step:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def step(self):
        time.sleep(3)
        step = AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="vitalgain.jp:id/main_dashboard_flex_layout"]/android.widget.FrameLayout[2]/android.view.ViewGroup'
        self.scroll_and_find.scroll_and_find(step)
        print("222")
        time.sleep(5)
        record_step = self.driver.find_element(AppiumBy.XPATH,
                                               '//android.webkit.WebView[@text="Step"]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.widget.TextView[2]')
        print("111")
        time.sleep(3)
        step_text = record_step.text
        print("Step:", step_text)

