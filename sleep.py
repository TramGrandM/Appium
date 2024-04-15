from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find
from scroll import Scroll
import time
from connect_db import connect
from convert_time import convert_time_2
from compare_sleep import compare_sleep


class Sleep:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)
        self.scroll = Scroll(self.driver)

    def sleep(self):
        element = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/dashboard_micro_title_tv" and @text="Sleep"]'
        self.scroll_and_find.scroll_and_find(element)
        time.sleep(8)
        # day_sleep = self.driver.find_element(AppiumBy.XPATH,
        #                                      '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[8]')
        # day_sleep.click()
        # time.sleep(3)
        time_sleep = self.driver.find_element(AppiumBy.XPATH,
                                              '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[11]/android.widget.TextView[2]')
        print("Time sleep:", time_sleep.text)
        self.scroll.scroll()
        total = self.driver.find_element(AppiumBy.XPATH,
                                         '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[15]/android.view.View[2]/android.view.View[1]/android.widget.TextView')
        total_str = total.text
        print("Total :", total_str)
        deep = self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[15]/android.view.View[2]/android.view.View[2]/android.widget.TextView')
        deep_str = deep.text
        print("Deep:", deep_str)
        light = self.driver.find_element(AppiumBy.XPATH,
                                         '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[15]/android.view.View[2]/android.view.View[3]/android.widget.TextView')
        light_str = light.text
        print("Light:", light_str)
        rem = self.driver.find_element(AppiumBy.XPATH,
                                       '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[15]/android.view.View[2]/android.view.View[4]/android.widget.TextView')
        rem_str = rem.text
        print("Rem:", rem_str)
        wake = self.driver.find_element(AppiumBy.XPATH,
                                        '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View[15]/android.view.View[2]/android.view.View[5]/android.widget.TextView')
        wake_str = wake.text
        print("Wake:", wake_str)
        # compare
        try:
            arr = connect("SELECT user_id, total_sleep_time, deep, light, rem , wake FROM user_health_source_sleep_history WHERE user_id = '2386' AND start_date = '2024-04-14 00:00:00' ")
            compare_sleep(arr, 1, total_str)
            compare_sleep(arr, 2, deep_str)
            compare_sleep(arr, 3, light_str)
            compare_sleep(arr, 4, rem_str)
            compare_sleep(arr, 5, wake_str)
        except Exception as e:
            print(e)
        finally:
            print("Sleep - Done!")


