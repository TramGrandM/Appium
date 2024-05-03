import random
import time

from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find


class Edit_profile:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)

    def edit_profile(self):
        edit = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/avatar_iv')
        edit.click()
        # # edit birthday
        # i = random.randint(1, 9)
        # birthday = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vitalgain.jp:id/edit_profile_iv"])[5]')
        # birthday.click()
        # date = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_birthday_tv"]')
        # date.clear()
        # date.send_keys(f'2001-0{i}-0{i}')
        # date.click()
        # ok_btn_1 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="vitalgain.jp:id/date_picker_ok"]')
        # ok_btn_1.click()
        # # month = self.driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="android:id/pickers"]/android.widget.NumberPicker[1]')
        # # month.send_keys('Jul')
        # # day = self.driver.find_element(AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="android:id/pickers"]/android.widget.NumberPicker[2]')
        # # day.send_keys(f'{i}')
        # # ok_btn_1 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="vitalgain.jp:id/date_picker_ok"]')
        # # ok_btn_1.click()
        # # print("111")
        # time.sleep(3)
        # # save = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/activity_update_apply"]')
        # # save.click()
        # # save
        # self.driver.tap([(665, 115)])
        # time.sleep(5)
        # # edit height
        # h = random.randint(140, 190)
        # height = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vitalgain.jp:id/edit_profile_iv"])[6]')
        # height.click()
        # height_input = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_height_edt"]')
        # height_input.clear()
        # height_input.send_keys(f'{h}')
        # time.sleep(3)
        # # save_1 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/activity_update_apply"]')
        # # save_1.click()
        # self.driver.tap([(665, 115)])
        # time.sleep(5)
        # # edit weight
        # w = random.randint(35, 90)
        # weight = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vitalgain.jp:id/edit_profile_iv"])[7]')
        # weight.click()
        # weight_input = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_weight_edt"]')
        # weight_input.clear()
        # weight_input.send_keys(f'{w}')
        # time.sleep(3)
        # # save_2 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/activity_update_apply"]')
        # # save_2.click()
        # self.driver.tap([(665, 115)])
        # time.sleep(5)
        # # edit waist
        # wa = random.randint(50, 100)
        # waist = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="vitalgain.jp:id/edit_profile_iv"])[8]')
        # waist.click()
        # waist_input = self.driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="vitalgain.jp:id/register_waist_edt"]')
        # waist_input.clear()
        # waist_input.send_keys(f'{wa}')
        # time.sleep(3)
        # # save_3 = self.driver.find_element(AppiumBy.XPATH,
        # #                                   '//android.widget.TextView[@resource-id="vitalgain.jp:id/activity_update_apply"]')
        # # save_3.click()
        # self.driver.tap([(665, 115)])
        # time.sleep(5)
        # # edit blood
        # blood = AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="vitalgain.jp:id/activity_edit_blood_type"]/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat'
        # self.scroll_and_find.scroll_and_find(blood)
        # # bl_array = ['A', 'B', 'C', 'AB', 'O']
        # # bl_input = random.choice(bl_array)
        # bl = random.randint(1,  4)
        # bl_drop = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="android:id/text1"]')
        # bl_drop.click()
        # time.sleep(3)
        # blood_input = self.driver.find_element(AppiumBy.XPATH, f'//android.widget.ListView/android.widget.TextView[{bl}]')
        # blood_input.click()
        # time.sleep(3)
        # # save_4 = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="vitalgain.jp:id/activity_update_apply"]')
        # # save_4.click()
        # self.driver.tap([(665, 115)])
        # time.sleep(3)
        # back = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        # back.click()
        # time.sleep(3)
        # back.click()
        # meal alert
        meal = AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="vitalgain.jp:id/activity_edit_meal_times"]/androidx.appcompat.widget.LinearLayoutCompat/androidx.appcompat.widget.LinearLayoutCompat'
        self.scroll_and_find.scroll_and_find(meal)
        time.sleep(3)
        breakfast = self.driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="vitalgain.jp:id/activity_update_meal_times_breakfast"]/androidx.appcompat.widget.LinearLayoutCompat/android.widget.EditText[1]')
        breakfast.click()
        print("111")
