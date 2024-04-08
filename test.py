import time

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from scroll import Scroll


class Test:
    def __init__(self, driver):
        self.driver = driver
        self.scroll = Scroll(self.driver)

    def scroll_and_find_all(self, element):
        while True:

            try:

                time.sleep(2)
                parent_element = self.driver.find_element(AppiumBy.XPATH, element)

                ele = parent_element.find_elements(AppiumBy.XPATH, ".//*")[-1]
                self.scroll.scroll()
                if ele.is_displayed():
                    self.scroll.scroll()
                    ele_1 = parent_element.find_elements(AppiumBy.XPATH, './/*')
                    for e in ele_1:
                        if e.text == "OFF":
                            e.click()
                            print(e.text)
                    break
            except IndexError:
                break



        # found_child_elements = []
        #
        # while True:
        #     elements = parent_element.find_elements(AppiumBy.XPATH, element)
        #
        #     for element in elements:
        #         is_displayed = element.is_displayed()
        #         # Do something with the element based on its displayed status
        #         if is_displayed:
        #             print("Displayed Element:", element.text)
        #         else:
        #             print("Not Displayed Element:", element.text)
        #
        #     # Perform a scroll gesture to load more elements
        #     self.scroll.scroll()
        #
        #     # Check if reached the end of parent element
        #     if len(elements) == len(parent_element.find_elements(AppiumBy.XPATH, element)):
        #         break
        # found_child_elements = []
        #
        # while not found_child_elements:
        #     elements = parent_element.find_elements(AppiumBy.XPATH, element)
        #
        #     if elements:
        #         found_child_elements.extend(elements)
        #
        #         print(len)
        #         for child in found_child_elements:
        #             print('Print:', child.text)
        #     else:
        #         self.scroll.scroll()

