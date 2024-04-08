from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from scroll import Scroll


class Scroll_and_Find:
    def __init__(self, driver):
        self.driver = driver
        self.scroll = Scroll(self.driver)

    def scroll_and_find(self, element):
        # element = AppiumBy.XPATH, '(//android.widget.Switch[@resource-id="vitalgain.jp:id/dashboard_settings_sw"])'
        found_element = False
        while not found_element:
            try:
                find_ele = self.driver.find_element(*element)
                found_element = True
                text = find_ele.text
                print("Text:", text)
                find_ele.click()
            except NoSuchElementException:
                self.scroll.scroll()

