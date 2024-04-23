import time
from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find
from connect_db import connect


class Health_Assessment:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def health_assessment(self):
        time.sleep(3)
        # element = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/dashboard_micro_title_tv" and @text="Health Assessment"]'
        element = AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/dashboard_micro_title_tv" and @text="総合健康スコア"]'
        self.scroll_and_find.scroll_and_find(element)
        time.sleep(10)
        title = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="総合健康スコア"]')
        title_text = title.text
        assert title_text == '総合健康スコア', 'Not same'
        rank = self.driver.find_element(AppiumBy.XPATH,
                                      '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.widget.TextView[6]')
        point = self.driver.find_element(AppiumBy.XPATH,
                                         '//android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.widget.TextView[3]')
        print("Ranking: ", rank.text, 'Point: ', point.text)
        # color = el.value_of_css_property('color')
        # print('color:', color)
        ranking = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="評価"]')
        btn_ranking = ranking.text
        assert btn_ranking == '評価', 'Not same'
        ranking.click()
        time.sleep(3)
        title_ranking = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="ランキング"]')
        tt_ranking = title_ranking.text
        assert tt_ranking == 'ランキング', 'Not same'
        y_rank = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="あなたの順位"]')
        text_y_rank = y_rank.text
        assert text_y_rank == 'あなたの順位', 'Not same'


