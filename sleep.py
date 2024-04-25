from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find
from scroll import Scroll
import time
from connect_db import connect
from convert_time import convert_time_2
from compare_sleep import compare_sleep
import datetime


class Sleep:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)
        self.scroll = Scroll(self.driver)

    def sleep(self):
        self.driver.implicitly_wait(5)
        element = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/dashboard_micro_title_tv" and @text="Sleep"]'
        self.scroll_and_find.scroll_and_find(element)
        time.sleep(8)
        # day_sleep = self.driver.find_element(AppiumBy.XPATH,
        #                                      '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[8]')
        # day_sleep.click()
        # time.sleep(5)
        # time_sleep = self.driver.find_element(AppiumBy.XPATH,
        #                                       '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[11]/android.widget.TextView[2]')
        self.scroll.scroll()
        time.sleep(10)
        total = self.driver.find_element(AppiumBy.XPATH,
                                         '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[15]/android.view.View[2]/android.view.View[1]/android.widget.TextView')
        total_str = total.text
        deep = self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[15]/android.view.View[2]/android.view.View[2]/android.widget.TextView')
        deep_str = deep.text
        light = self.driver.find_element(AppiumBy.XPATH,
                                         '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[15]/android.view.View[2]/android.view.View[3]/android.widget.TextView')
        light_str = light.text
        rem = self.driver.find_element(AppiumBy.XPATH,
                                       '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[15]/android.view.View[2]/android.view.View[4]/android.widget.TextView')
        rem_str = rem.text
        wake = self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[15]/android.view.View[2]/android.view.View[5]/android.widget.TextView')
        wake_str = wake.text
        # compare
        today = datetime.date.today()
        try:
            arr = connect(f"SELECT user_id, total_sleep_time, deep, light, rem , wake FROM user_health_source_sleep_history WHERE user_id = '19778' AND start_date = '{today} 00:00:00' ")
            compare_sleep(arr, 1, total_str)
            compare_sleep(arr, 2, deep_str)
            compare_sleep(arr, 3, light_str)
            compare_sleep(arr, 4, rem_str)
            compare_sleep(arr, 5, wake_str)
        except Exception as e:
            print(e)
        finally:
            print("Sleep - Done!")


