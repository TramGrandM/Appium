import time

from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find
from scroll import Scroll


class BloodPressure:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)
        self.scroll = Scroll(self.driver)

    def bloodPressure(self):
        element = AppiumBy.XPATH, '//android.widget.TextView[@text="Blood pressure"]'
        self.scroll_and_find.scroll_and_find(element)
        add = self.driver.find_element(AppiumBy.XPATH,
                                       '//android.widget.Button[@resource-id="vitalgain.jp:id/blood_pressure_add_btn"]')
        add.click()
        sys = self.driver.find_element(AppiumBy.XPATH,
                                       '//android.widget.EditText[@resource-id="vitalgain.jp:id/dialog_blood_pressure_systolic_edt"]')
        sys.send_keys(120)
        dia = self.driver.find_element(AppiumBy.XPATH,
                                       '//android.widget.EditText[@resource-id="vitalgain.jp:id/dialog_blood_pressure_diastolic_edt"]')
        dia.send_keys(80)
        add_img = self.driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.ImageView[@resource-id="vitalgain.jp:id/holder_blood_pressure_add_iv"]')
        add_img.click()
        select = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Select photos"]')
        select.click()
        img = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Image"])[1]')
        img.click()
        add_btn = self.driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.Button[@resource-id="vitalgain.jp:id/dialog_add_btn"]')
        add_btn.click()
        time.sleep(2)
        back = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        back.click()
        print('Blood Pressure - Done! ')
