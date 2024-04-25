import random
import time

from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find


class Edit_profile:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def edit_profile(self):
        # edit = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/avatar_iv')
        # edit.click()
        # edit birthday
        i = random.randint(1, 12)
        birthday = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vitalgain.jp:id/edit_profile_iv"])[5]')
        birthday.click()
        date = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_birthday_tv"]')
        date.clear()
        date.send_keys(f'2001-{i}-06')
        date.click()
        ok_btn_1 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="vitalgain.jp:id/date_picker_ok"]')
        ok_btn_1.click()
        save = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/activity_update_apply"]')
        save.click()
        time.sleep(5)
        # edit height
        h = random.randint(140, 190)
        height = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vitalgain.jp:id/edit_profile_iv"])[6]')
        height.click()
        height_input = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_height_edt"]')
        height_input.clear()
        height_input.send_keys(f'{h}')
        save_1 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/activity_update_apply"]')
        save_1.click()
        time.sleep(5)
        # edit weight
        w = random.randint(35, 90)
        weight = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vitalgain.jp:id/edit_profile_iv"])[7]')
        weight.click()
        weight_input = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_weight_edt"]')
        weight_input.clear()
        weight_input.send_keys('5')
        save_2 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/activity_update_apply"]')
        save_2.click()
        time.sleep(5)
        # edit waist
        wa = random.randint(50, 100)
        waist = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vitalgain.jp:id/edit_profile_iv"])[8]')
        waist.click()
        waist_input = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_waist_edt"]')
        waist_input.clear()
        waist_input.send_keys(f'{wa}')
        save_3 = self.driver.find_element(AppiumBy.XPATH,
                                          '//android.widget.TextView[@resource-id="vitalgain.jp:id/activity_update_apply"]')
        save_3.click()
        time.sleep(5)
        # edit blood
        blood = AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vitalgain.jp:id/edit_profile_iv"])[5]'
        self.scroll_and_find.scroll_and_find(blood)
        bl_array = ['A', 'B', 'C', 'AB', 'O']
        bl_input = random.choice(bl_array)
        blood_input = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1"]')
        blood_input.clear()
        blood_input.send_keys(bl_input)
        save_4 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/activity_update_apply"]')
        save_4.click()

        back = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        back.click()
