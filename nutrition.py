from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find
from scroll import Scroll
import time
from connect_db import connect
from convert_time import convert_time_2
from compare_sleep import compare_sleep


class Nutrition:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)
        self.scroll = Scroll(self.driver)

    def nutrition(self):
        element = AppiumBy.XPATH, '//android.widget.TextView[@text="Nutrition"]'
        self.scroll_and_find.scroll_and_find(element)
        print("Aaa11111111111")

