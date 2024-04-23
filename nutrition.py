import time

from appium.webdriver.common.appiumby import AppiumBy
from scroll_and_find import Scroll_and_Find
from scroll import Scroll


class Nutrition:
    def __init__(self, driver):
        self.driver = driver
        self.scroll_and_find = Scroll_and_Find(self.driver)
        self.scroll = Scroll(self.driver)

    def nutrition(self):
        element = AppiumBy.XPATH, '//android.widget.TextView[@text="Nutrition"]'
        self.scroll_and_find.scroll_and_find(element)
        add = self.driver.find_element(AppiumBy.XPATH,
                                       '(//android.widget.ImageView[@resource-id="vitalgain.jp:id/edit_iv"])[1]')
        add.click()
        manual = self.driver.find_element(AppiumBy.XPATH,
                                          '//androidx.appcompat.widget.LinearLayoutCompat[@resource-id="vitalgain.jp:id/section_add_manual_l"]/android.widget.ImageView')
        manual.click()
        # add food
        name = self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.EditText[@resource-id="vitalgain.jp:id/dialog_add_food_name_food_edt"]')
        name.send_keys('Mi')
        calories = self.driver.find_element(AppiumBy.XPATH,
                                            '//android.widget.EditText[@resource-id="vitalgain.jp:id/dialog_add_food_cal_edt"]')
        calories.send_keys(150)
        protein = self.driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.EditText[@resource-id="vitalgain.jp:id/dialog_add_food_protein_edt"]')
        protein.send_keys(10)
        fat = self.driver.find_element(AppiumBy.XPATH,
                                       '//android.widget.EditText[@resource-id="vitalgain.jp:id/dialog_add_food_fat_edt"]')
        fat.send_keys(10)
        carbon = self.driver.find_element(AppiumBy.XPATH,
                                          '//android.widget.EditText[@resource-id="vitalgain.jp:id/dialog_add_food_carb_edt"]')
        carbon.send_keys(10)
        natrium = self.driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.EditText[@resource-id="vitalgain.jp:id/dialog_add_food_natrium_edt"]')
        natrium.send_keys(10)
        desc = self.driver.find_element(AppiumBy.XPATH,
                                        '//android.widget.EditText[@resource-id="vitalgain.jp:id/dialog_add_food_description_edt"]')
        desc.send_keys("Miiiii")
        add_img = self.driver.find_element(AppiumBy.XPATH,
                                           '//android.widget.ImageView[@resource-id="vitalgain.jp:id/holder_nutrition_add_image_iv"]')
        add_img.click()
        select = self.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Select photos"]')
        select.click()
        if self.driver.find_element(AppiumBy.ID, 'com.android.packageinstaller:id/permission_allow_button').is_displayed():
            self.driver.find_element(AppiumBy.ID, 'com.android.packageinstaller:id/permission_allow_button').click()
        img = self.driver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Image"])[1]')
        img.click()
        choice = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/menu_done')
        choice.click()
        add_btn = self.driver.find_element(AppiumBy.ID, 'vitalgain.jp:id/dialog_add_food_add_btn')
        add_btn.click()
        time.sleep(3)
        self.driver.back()
        time.sleep(2)
        back = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        back.click()
        print("Nutrition - Done!")
