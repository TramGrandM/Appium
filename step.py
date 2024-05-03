import datetime
import time
from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find
from connect_db import connect


class Step:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def step(self):
        time.sleep(3)
        element = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/dashboard_micro_title_tv" and @text="Step"]'
        self.scroll_and_find.scroll_and_find(element)
        time.sleep(10)
        # day = self.driver.find_element(AppiumBy.XPATH,
        #                                '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[9]')
        # day.click()
        self.driver.tap([(470, 790)])
        time.sleep(10)
        record_step = self.driver.find_element(AppiumBy.XPATH,
                                               '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.TextView[6]')
        time.sleep(3)
        step_text = record_step.text
        convert_step = step_text.replace(",", "")
        activity = self.driver.find_element(AppiumBy.XPATH,
                                            '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.widget.TextView[3]')
        activity_text = activity.text
        # compare
        try:
            today = datetime.date.today()
            date = today - datetime.timedelta(days=1)
            arr = connect(
                f"SELECT step, activity_time FROM user_health_source_step_history WHERE user_id = 19778 AND start_date = '{date} 00:00:00'")
            for a in arr:
                assert a[0] == int(convert_step), "Step not equal"
                print('step:', a[0])
                if activity_text == '--':
                    activity_text = 'NULL'
                    assert a[1] == activity_text, "Activity time not equal"
                    print('Activity:', a[1])
                else:
                    act = round(a[1] / 60)
                    assert int(activity_text) == act, "Activity time not equal"
                    print('Activity:', act)

        except Exception as e:
            print("Exception:", e)
        finally:
            print("Step - Done!")
